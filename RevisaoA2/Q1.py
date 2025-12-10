from abc import ABC, abstractmethod

class FitSquareError(Exception): ...
class PlanError(FitSquareError): ...
class ExtraNotFoundError(PlanError): ...
class FeatureNotFoundError(PlanError): ...

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
    
    @classmethod
    def add_feature(cls, feature):
        cls.stand_features = cls.stand_features + feature

class PremiumPlan(Plan):
    stand_features = ["Personal"]
    def __init__(self, base_price):
        self._plan_type = "Premium"  # "basic" ou "premium"
        self._price = base_price
        self._extras = [] 

        
class BasicPlan(Plan):
    stand_features = []
    def __init__(self, base_price):
        self._plan_type = "Basic"  # "basic" ou "premium"
        self._price = base_price
        self._extras = []


class Member:
    def __init__(self, name, email, plan : BasicPlan | PremiumPlan):
        self._name = name
        self._email = email
        self._plan = plan
        self._features = ["aulas em grupo"]
    
    def name(self):
        return self._name

    @property
    def plan(self):
        return self._plan
    
    @plan.setter
    def plan(self, plan):
        self._plan = plan

    def features(self):
        return self._features + self.plan.__class__.stand_features

    def rm_features(self, features):
        if isinstance(features, list):
            for feature in features:
                if feature in self._features:
                    self._features.remove(feature)
                raise ExtraNotFoundError("This extra doesn't exist")
        elif features in self._features:
            self._features.remove(features)
        else:
            raise ExtraNotFoundError("This extra doesn't exist")

    def add_features(self, features):
        if isinstance(features, list):
            for feature in features:
                self._features.append(feature)
        else:
            self._features.append(features)


    def upgrade_features(self):
        self.add_features(self.plan.extras)


    def upgrade_plan(self, new_plan : BasicPlan | PremiumPlan):
        old_price = self.plan.get_total_price()
        new_price = new_plan.get_total_price()
        diff = new_price - old_price
        string = f"{self.name()} está mudando de {self.plan.plan_type()} para {new_plan.plan_type()}.\nPreço antigo: R$ {old_price}, novo preço: R$ {new_price}. Diferença: R$ {diff}."
        self.plan = new_plan
        self.upgrade_features()
        return string

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


# Não mexi no SubscriptionService mas ele poderia ter mais funções (quebra o SRP)

#Driver Code

plano1 = BasicPlan(100)
plano2 = PremiumPlan(200)
ana = Member("ana", "ana@gmail", plano1)
print(plano1.available_extras)
print(plano1.extras)
#print(plano1.add_extras("nutri")) quebra o programa
print(plano1.add_extras("nutricao"))
print(plano1.extras)

print(ana.features())
print(ana.add_features("bike"))
print(ana.features())
#print(ana.rm_features("caminhada")) quebra o programa aqui
print(ana.describe_features())
print(ana.rm_features("bike"))
print(ana.describe_features())
print(ana.upgrade_plan(plano2))