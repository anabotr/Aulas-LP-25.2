#Estamos usando como base o código do arquivo "aula21-bank_oo.py", qualquer 
# dúvida sobre o funcionamento deve ser consultada lá

from datetime import datetime

class BankingError(Exception): pass
class NegativeAmountError(BankingError): pass 
class InsufficientFundsError(BankingError): pass

#OCP


class Account:
    def __init__(self, owner: str, currency: str = "BRL", 
                 initial_balance: float = 0.0):

        #Precisamos encpsular: _tatata isso diz pra qualquer programadaor que o 
        # método é protegido
        self._customer = owner
        self._currency = currency
        self._balance = float(initial_balance)
        self._created_at = datetime.now().isoformat(timespec = "seconds")
        self._customer.add_account(self)

    
    def deposit(self, amount : float) -> None:
        if amount <= 0:
            raise NegativeAmountError("[ERROR] Deposit must be positive.")
        self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, amount : float) -> None:
        if amount <= 0:
            raise NegativeAmountError("[ERROR] Withdrawal must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError("[ERROR] Insufficient funds.")
        
        self.balance = self.balance - amount
        return self.balance
    

    def __str__(self) -> str:
        return f"Account (owner= {self.customer}), currency = {self.currency}, balance = {self.balance}"


    @property
    def balance(self) -> float:
        return self._balance
    
    @balance.setter
    def balance(self, new_balance: float) -> None:
        if new_balance != new_balance:
            return BankingError("[ERROR] Balance cannot be set to NaN.")
        self._balance = float(new_balance)
        return

    def monthly_update(self) -> None:
        print(f"A classe {self.__class__.__name__} não precisa de atualização mensal")
    
        
    
class Customer:
    #Aqui, também encapsulamos
    def __init__(self, name: str, email: str):
        self._name = name
        self._email = email
        self._accounts: list[Account] = []
    
    def add_account(self, account: Account):
        if account not in self._accounts:
            self._accounts.append(account)
    
    @property
    def accounts(self) -> list[Account]:
        return list(self._accounts)

acc1 = Account("Ana", "BRL", 20.0)
acc2 = Account("Vitória", "USD", 10.0) 
print(acc1)
acc1.deposit(1000)
acc2.deposit(300)
acc1.withdraw(1015)
acc1.balance = 10000
print(acc1.balance)