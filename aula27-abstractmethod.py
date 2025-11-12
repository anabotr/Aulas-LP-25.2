from abc import ABC, abstractmethod

#Uma classe asbtrata é uma classe que não pode ser instanciada
#A única maneira de fazer isso em python é usando o ABC (Abstract Base Class) 
# do módulo abc, daí, todos os filhos herdarão isto


#IST: Princípio de Segregação das Interfaces
#Quando temos uma nterface enorme, temos vários métodos que seremos obrigados a
# implementar, segregando, teremos vários derivados que poderemos escolher


class AccountBAD(ABC):
    @abstractmethod #é um método que não tem corpo, ele está aqui para que
    # os filhos de account implementem, o que implementar, será o primeiro
    # filho concreto de account, os que não implementam dá erro
    def deposit(self, amount: float): ... #Estamos fazendo um método abstrato
    
    @abstractmethod
    def withdraw(self, amount: float): ...
    
    @abstractmethod
    def apply_interest(self, amount: float): ...
        
    @abstractmethod
    def charge_fee(self, amount: float): ...
    
    #Podemos ter mais coisas concretas aqui, um abstrato torna ela abstrata
    
class SavingsAccountBAD(AccountBAD):
    def deposit(self, amount: float): print(f"Depositando{amount}")
    
    def withdraw(self, amount: float): print(f"Sacando {amount}")
    
    def apply_interest(self, amount: float): print("Aplicando juros")
    
    #eu tenho um método que não serve para nada nesta classe, está errado
    def charge_fee(self, amount: float): print("Nada a cobrar")
    
class CheckingAccountBAD(AccountBAD):
    def deposit(self, amount: float): print(f"Depositando{amount}")
    
    def withdraw(self, amount: float): print(f"Sacando {amount}")
    
    #não existe rendimento em cima de conta salário
    def apply_interest(self, amount: float): print("Nada a fazer")
    
    def charge_fee(self, amount: float): print("Cobrando a taxa mensal")
    
# acc1 = AccountBAD()
# print(acc1)

#------------------------------------------------------------------------------
#Aqui, vamos criar 4 interfaces para resolver o problemaque tínhamos 
# anteriormente, a orientação a objetos deve ser "redonda"

class Depositable(ABC):
    @abstractmethod 
    def deposit(self, amount: float): ...
    
class Withdrawable(ABC):
    @abstractmethod
    def withdraw(self, amount: float): ...

class InterestBearing(ABC):
    @abstractmethod
    def apply_interest(self, amount: float): ...
        
class FeeChargeable(ABC):
    @abstractmethod
    def charge_fee(self, amount: float): ...
    
class SavingsAccount(Depositable, Withdrawable, InterestBearing):
    def deposit(self, amount: float): print(f"Depositando{amount}")
    
    def withdraw(self, amount: float): print(f"Sacando {amount}")
    
    def apply_interest(self, amount: float): print("Aplicando juros")

    
class CheckingAccount(Depositable,  Withdrawable, FeeChargeable):
    def deposit(self, amount: float): print(f"Depositando{amount}")
    
    def withdraw(self, amount: float): print(f"Sacando {amount}")
    
    def charge_fee(self, amount: float): print("Cobrando a taxa mensal")
    
class InvestmentAccount(Depositable, Withdrawable, InterestBearing, FeeChargeable):
    def deposit(self, amount: float): print(f"Depositando{amount}")
    
    def withdraw(self, amount: float): print(f"Sacando {amount}")
    
    def apply_interest(self, amount: float): print("Aplicando juros")
    
    def charge_fee(self, amount: float): print("Cobrando a taxa mensal")
    
#Toda a vez que eu crio uma classe de conta nova no banco, eu defino que coisas
# essa classe terá. Dizemos que a classe será "sacável", "depositável", etc
#Quando as "classes" viram adjetivos, chamamos de INTERFACE (como o depositable,
# withdrawable, etc)


###############################################################################
#Driver Code

savings = SavingsAccount()
checking = CheckingAccount()
investment = InvestmentAccount()

savings.apply_interest(6)
checking.charge_fee(20)
investment.apply_interest(10)
investment.charge_fee(100)


















