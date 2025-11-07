#a classe herda do object por padrão
class Guerreiro:
    def __init__(self, nome):
        self.nome = nome
        self._arma = None
        #o init não retorna nada!
    
    def atacar(self):
        if self._arma is not None:
            print(f"{self.nome} ataca com {self._arma.nome}")
        else:
            print(f"{self.nome} ataca com as próprias mãos")
    
    def __del__(self):
        print(f"Removendo {self.nome}")
        
    def equipar_arma(self, nome):
        self._arma = Arma(nome)
        
class Arma:
    def __init__(self, nome):
        self.nome = nome
    
    def __str__(self):
        print(f"Eu sou a arma {self.nome}")
    
    def __del__(self):
        print(f"Removendo {self.nome}")

guerreiro_1 = Guerreiro("Miyamoto Musashi")
guerreiro_1.atacar()
guerreiro_1.equipar_arma("Wakizashi")
guerreiro_1.atacar()
guerreiro_1.equipar_arma("Katana") #quando reequipamos, criamos um objeto novo,
# colocamos dentro do ciclo de vida de guerreiro_1 e a outra é apagada

#TODO: descobrir como apagar apenas a arma com del

del guerreiro_1 #apaga também a arma, ou seja, se o objeto maior é deletado, os 
# outros criados a partir dele e relacionados a ele também são deletados
#Essa relação é de composição!!!!!
#Na agregação, os objetos tem vida independente e são usados para compor uma
# coisa maior