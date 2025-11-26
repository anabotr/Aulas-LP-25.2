from abc import ABC, abstractmethod

class FitSquareError(Exception): ...
class PlanError(FitSquareError): ...
class ExtraNotFoundError(PlanError): ...

class Plan(ABC):
    available_extras = {
    "nutricao": 50,
    "massagem": 80,
    "pilates": 40,
    "avaliacao": 60,
}
    
    def get_total_price(self):
        extras_value = sum(Plan.available_extras[e] for e in self.extras)
        return self.price + extras_value
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price
    
    @property
    def extras(self):
        return self._extras

    @classmethod
    def get_prize_extra(cls, extra):
        for ext in cls.extras:
            if ext[0] == extra:
                return float(ext[1])
        return None

    def add_extras(self, extras):
        if not isinstance(extras, list):
            extras = [extras]
        
        for extra in extras:
            if extra not in Plan.available_extras:
                raise ExtraNotFoundError(f"Extra inválido: {extra}")
            self._extras.append(extra)
        
    def plan_type(self):
        return self._plan_type

class PremiumPlan(Plan):
    def __init__(self, base_price):
        self._plan_type = "Premium"  # "basic" ou "premium"
        self._price = base_price
        self._extras = []            # lista de strings
    

        
class BasicPlan(Plan):
    def __init__(self, base_price):
        self._plan_type = "Basic"  # "basic" ou "premium"
        self._price = base_price
        self._extras = []            # lista de strings


class Member:
    def __init__(self, name, email, plan : BasicPlan | PremiumPlan):
        self._name = name
        self._email = email
        self._plan = plan
        self._features = ["aulas em grupo"]
    
    @property
    def plan(self):
        return self._plan
    
    @plan.setter
    def plan(self, plan):
        self._plan = plan

    def features(self):
        return self._features

    def rm_features(self, features):
        if isinstance(features, list):
            for feature in features:
                self.features.remove(feature)
        else:
            self.features.remove(features)

    def add_features(self, features):
        if isinstance(features, list):
            for feature in features:
                self.features.append(feature)
        else:
            self.features.append(features)


    def upgrade_features(self):
        if self.plan.plan_type() == "Premium":
            self.add_features("Personal")
        else:
            if "Personal" in self.features:
                self.rm_features("Personal")
        for extra in self.plan.extras:
            self.add_features(extra)


    def upgrade_plan(self, new_plan : BasicPlan | PremiumPlan):
        old_price = self.plan.get_total_price()
        new_price = new_plan.get_total_price()
        diff = new_price - old_price
        self.plan = new_plan
        self.upgrade_features()

        return f"{self.name} está mudando de {self.plan.plan_type()} para {new_plan.plan_type()}.\nPreço antigo: R$ {old_price}, novo preço: R$ {new_price}. Diferença: R$ {diff}."


    def describe_features(self):
        return self._features

class SubscriptionService:
    def process_upgrade(self, member, new_plan):
        # lógica de log acoplada ao serviço
        with open("subscriptions.log", "a") as f:
            f.write(
                f"{member.name} -> {new_plan.plan_type()} "
                f"(extras: {new_plan.extras}, total: {new_plan.get_total_price()})\n"
            )

        # lógica de cálculo deixada no Member
        member.upgrade_plan(new_plan)

        print("Upgrade concluído!")