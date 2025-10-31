#Aulas 21, 22 e 23! - encapsulamento

# queremos fazer a tarnsição de um sistema procedural para um sistema orientado
#a objetos

#objetos têm estados, que são valores/características, exemplo, string = "Ana"
#eles também têm comportamentos, por exemplo, string.lower()

#a classe diz pro python como criar um objeto com determinados comportamentos
#e atributos

#o princípio de responsabilidade única diz que cada método deve ter o mínimo de
# responsabilidades, então, por exemplo, aqueles métodos que retornavam uma
# string explicando o que foi feito, agora vai retornar apenas o resultado 
# gerado e aquela string vai ser trabalho de outro método

from datetime import datetime

#a classe exception pode receber uma string, e seus descendentes herdam isso
class BankingError(Exception): #essa classe herda de exception, banking error 
# vai ser filho dele
    pass
class NegativeAmountError(BankingError): pass #esse é filho de banking error
class InsufficientFundsError(BankingError): pass
    

#classes precisam de docstring (que não terminamos de completar, mas pode ter 
#até doctest)
class Account:
    """
    Representa uma conta bancária simples.
    
    Attributes:
        owner (str): Name of the account holder.
        currency (str): Account currency code (e.g. "BRL", "USD").
        balance (float): Current balance of the account.
        
    Methods:
        deposit(amount): ...
        withdraw(amount): ...
        show_balance(): ...
    
    Example:
        >>>...
    """
    #cada classe deve ter apenas uma responsabilidade (propósito)
    
    
    #init é o primeiro método que criamos, ele é chamado automaticamente quando
    #chamamos a classe
    
    #self é o objeto sobre o qual init vai operar, ele não cria o objeto, pega
    #algo já pronto e inicializa
    def __init__(self, owner: str, currency: str = "BRL", 
                 initial_balance: float = 0.0):
        """
        docstring que não vamos fazer agora!

        Parameters
        ----------
        owner : str
            DESCRIPTION.
        currency : str, optional
            DESCRIPTION. The default is "BRL".
        intial_balance : float, optional
            DESCRIPTION. The default is 0.0.

        Returns
        -------
        None.

        """
        
        #o init pega o valor que te interessa e encaixa no objeto que foi dado
        
        #abaixo estamos criando um atributo, se o atributo owner já exite, ele
        #sobrescreve, senão, ele cria
        self.customer = owner
        self.currency = currency
        
        self._balance = float(initial_balance) #usar um underscore significa
        #que o atributo é protegido e só deve ser modificado dentro da classe
        #(e não no driver code) as classes filhas herdam.
        #Apesar de mutável, chamamos balance de membro de dados PROTEGIDO
        #Em outras linguagens de programação, apenas a classe em que um membro
        #de dados privado foi criado pode mudá-lo.
        #Se usamos dunder, criamos uma camada de dificuldade mas ainda é 
        #possível mudar o atributo de fora da classe, ele se torna privado, as 
        #classes filhas não herdam
        
        #Para acessar um dado privado/protegido, criamos um ponto de acesso
        #(método) público para acessá-lo
        
        self.created_at = datetime.now().isoformat(timespec = "seconds")
        #created_at, por exemplo, é um membro de dados PUBLICO
        
        #TODO: Mudar todos os atributos de self para serem membros de dados protegidos!!
        
        #todo o objeto da classe account vai ter o atributo fgv com valor 
        #"Carlos Ivan"
        #self.fgv = "Carlos Ivan"
        
        if hasattr(self.customer, "add_account"):
            self.customer.add_account(self)
        
        print(f'[INFO] Account created for {self.customer} in {self.currency} currency.')
    
    #Ainda não criamos métodos para a nossa classe account, mas ele tem um pai
    #"por debaixo dos panos", do qual ele herda vários métodos: veja dir(acc1)
    
    #agora, faremos um método normal (sem dunder)
    
    def deposit(self, amount : float) -> None:
        if amount <= 0:
            raise NegativeAmountError("[ERROR] Deposit must be positive.")
        self.balance = self.balance + amount #quando atribuimos, ele 
        #automaticamente chama o setter, quando não o fazemos, ele chama o 
        #getter
        return self.balance
    
    def withdraw(self, amount : float) -> None:
        if amount <= 0:
            raise NegativeAmountError("[ERROR] Withdrawal must be positive.")
        if amount > self.balance:
            raise InsufficientFundsError("[ERROR] Insufficient funds.")
        
        self.balance = self.balance - amount
        return self.balance
    
    #tínhamos um método que printava e mudamos para que usássemos um método já
    # existente e modificássemos ele de modo a retornar um objeto legível para 
    # humanos
    def __str__(self) -> str:
        return f"Account (owner= {self.customer}), currency = {self.currency}, balance = {self.balance}"
    
        
    #Toda a vez que atribuirmos alguma coisa a _balance, se executarão as 
    #funções seguintes
    
    @property #estamos dizendo que isso é uma propriedade de balance, ou seja,
    #nesse programa, quando chamamos account.balance, rodamos a função abaixo
    def balance(self) -> float:
        #SE O BALANCE ESTIVESSE PROTEGIDO! precisaríamos de um método público
        #para acessá-lo
        #poderíamos preparar o saldo antes de entregar 
        return self._balance
    
    @balance.setter
    def balance(self, new_balance: float) -> None:
        #SE O BALANCE ESTIVESSE PROTEGIDO! precisaríamos de um método público
        #para alterá-lo
        if new_balance != new_balance: #só entra se for NaN
            return BankingError("[ERROR] Balance cannot be set to NaN.")
        self._balance = float(new_balance)
        return
        
    
class Customer:
    """docstring lindo"""
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self._accounts: list[Account] = [] #o costumer tem uma lista de 
        #elementos do tipo account, que está vazia
    
    def add_account(self, account: Account): #isso é um MÉTODO
        if account not in self._accounts:
            self._accounts.append(account)
    
    @property
    def accounts(self) -> list[Account]:
        #vai listar as contas de um cliente
        return list(self._accounts)
        
#Há tipos de relação entre classes, usaremos agregação, que será explicada em
#outro doc (aula 22)
    
    
    
 
    
 
    
#Driver Code
acc1 = Account("Ana", "BRL", 20.0)
acc2 = Account("Vitória", "USD", 10.0) 

#o objeto que criamos tem atributos facilmente mutáveis, o que pode ser ruim
#portanto, precisamos encapsular algumas coisas. Usamos o _ pra isso.

acc1._balance += 1000 #isso não deveria ser possível, mas o python é permissivo
#ou seja, o underscore é apenas uma convenção. Em linguagens como Java e C++,
#de fato não é possível proteger.

#Agora, quando usamos acc1.__balance, ele cria uma camada a mais de dificuldade, 
#mas não dá de fato pra proteger o dado.
#Colocamos uma camada a mais de dificuldade para a pessoa que está usando 
#perceber que ele não deveria estar mexendo naquilo, porque é algo privado, mas 
#não há como de fato proibir.

print(acc1)
acc1.deposit(1000) #o python automaticamente faz self = acc1
acc2.deposit(300)
acc1.withdraw(1015)
acc1.balance = 10000
print(acc1.balance)