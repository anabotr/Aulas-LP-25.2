#A única coisa que é importante é como estamos organizando o código e os 
# metodos, neste arquivo. As funções em si não.

class Customer:
    def __init__(self, name):
        self._name = name
        self._accounts = []
    
    def add_account(self, account):
        print(f"[Customer] Associando conta \"{account.__class__.__name__}\" a {self._name}")
        #account.__class__.__name__ vai nos trazer a discussão sobre 
        # polimorfismo
        self._accounts.append(account)
        
    def accounts(self):
        return self._accounts

class Account:
    def __init__(self, customer):
        self._customer = customer
        customer.add_account(self)
        
    def deposit(self, amount):
        print(f"[{self.__class__.__name__}] Depósito simulado de {amount} unidades monetárias")
    
    def withdraw(self, amount):
        print(f"[{self.__class__.__name__}] Saque simulado de {amount} unidades monetárias")
    
    def monthly_update(self):
        print(f"[{self.__class__.__name__}] Nenhuma atualização mensal definida (MOCK, STUB)")
        #MOCK/STUB é um método que não serve pra nada, é um cotoco no seu 
        # código.
        #Se isso existe no seu código, você sabe que sua modelagem OO está ruim

###############################################################################

class SavingsAccount(Account):
    def withdraw(self, amount):
        print("[SavingsAccount] Saque autorizado apenas se houver saldo suficiente")
        #o código é importante se e somente se ele verifica o saldo
        print(f"(Simulação) {self._customer.__name__} tenta sacar {amount}")
        
    def monthly_update(self):
        print("[SavingsAccount] Aplicando juros mensais simulados")
        
#Polimorfismo: "irmãos", que, em tese fazem a mesma coisa mas de formas 
# diferentes
#No nosso exemplo, fizemos polimorfismo entre SavingsAccount e CheckingsAccount

class CheckingsAccount(Account):
    def withdraw(self, amount):
        print("[CheckingsAccount] Saque autorizado até o limite de crédito")
        print(f"(Simulação) {self._customer._name} tenta sacar {amount}")
        
    def monthly_update(self):
        print("[CheckingsAccount] Verificando e cobrando taxas necessárias")
        
class InvestmentAccount(Account):
    def simulate_yield(self): #Aqui, estamos criando um método que nenhum dos
    # irmãos tem, isso significa que a classe Account é aberta para extensão
    #Quando você faz uma classe bem feita, você tem que permitir que as pessoas
    # consigam adicionar comportamento aos objetos. Ainda, uma classe tem que 
    # estar fechada para modificação, não podemos usar uma subclasse para 
    # afetar uma superclasse, forçando ela a mudar, por exemplo. Isso é OCP: 
    # Open Closed Principle
        print("[InvestmentAccount] Simulando rendimento anual")

###############################################################################

class BankUtils: #Usamos a classe de Utils para juntar métodos importantes
    @staticmethod    
    def _print_account_details(account): #Aqui não tem self porque usamos essa
        # classe para agrupar funções que ficariam "jogadas" 
        #Ele vai ser um método estático, que será invocado a partir do nome da 
        # classe
        print(f"   -{account.__class__.__name__}")
    
    @staticmethod
    def _print_customer_summary(customer):
        for account in customer.accounts():
            BankUtils._print_account_details(account)
    
    @staticmethod
    def _monthly_update_all(customers):
        for customer in customers:
            for account in customer.accounts():
                account.monthly_update()
                
###############################################################################

class CryptoAccount(Account): #Eu consegui criar um tipo novo de conta: aberto 
# à extensão.
#Eu não modifiquei a classe Account: fechado para modificação.
#Segue o OCP!
    def withdraw(self, amount):
        print("[CryptoAccount] Saque de criptomoeda")
        print("Taxa de operação simulada")
        
    def monthly_update(self):
        print("[CryptoAccount] Sincronizando transações")

###############################################################################

customer_1 = Customer("Pedro")
customer_2 = Customer("Alejandra")
customer_3 = Customer("Ana Beatriz")

acc1 = SavingsAccount(customer_1)
acc2 = CheckingsAccount(customer_2)
acc3 = InvestmentAccount(customer_3)

acc5 = CryptoAccount(customer_3) #Se você adiciona esta nova classe, coloca uma
# conta nova e dá certo, significa que sua OO está correta no Solid

acc1.deposit(100)
acc2.withdraw(200)
acc3.simulate_yield()
acc5.withdraw(0.5)

#Contas diferentes que herdam de uma mesma classe se comportando de maneira 
# diferente no código, mas conseguimos usar métodos unificados para todas elas:
# repare que os métodos de BankUtils funcionam para todas elas, mesmo sendo 
# diferentes.
print("Customer 1:")
BankUtils._print_customer_summary(customer_1)
print("Customer 2:")
BankUtils._print_customer_summary(customer_2)
print("Customer 3:")
BankUtils._print_customer_summary(customer_3)

#Eu não tenho que saber que conta é de que para realizar os métodos, isos é 
# POLIMORFISMO!!
BankUtils._monthly_update_all([customer_1, customer_2, customer_3])

###############################################################################

class DeuRuimAccount(Account): #Vamos violar o Princípio de Substituição de 
# Liskov (LSP): Em qualquer programa, devemos conseguir substituir um objeto da 
# classe pai por um objeto da classe filho sem problemas. Se no seu programa um
# objeto de conta genérico ao se tornar um objeto de conta poupança quebra o 
# programa, você quebrou o princípio e essa não é uma boa modelagem de OO.
#O objeto filho também tem que poder ser substituído pelo pai.
    def withdraw(self, amount):
        print("[DeuRuimAccount] Saque sem restrições")
        #A superclasse diz que o saque tem limite e a subclasse desrespeita 

###############################################################################

acc4 = DeuRuimAccount(customer_3)
acc4.withdraw(40000000)
#Criamos um objeto DeuRuimAccount e quebramos o LSP
acc = Account(Customer("Carlos Ivan"))
acc6 = Account(Customer("Carlos Ivan"))
acc = acc5 #Isso funciona, LSP respeitado!
acc6 = acc4 #Isso funciona porque nesse código não há verificação, mas em um 
#banco com código, quebraria.
