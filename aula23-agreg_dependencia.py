#a ideia é criar uma classe que represente um grupo de aventureiros
class Guerreiro:
    def __init__(self, nome):
        self._nome = nome
        self._arma = None
        
    def atacar(self):
        if self._arma is not None:
            print(f"{self._nome} ataca com sua arma e causa (10) ponto(s) de dano.")
        else:
            print(f"{self._nome} ataca com as mãos e causa (1) ponto de dano.")

class Feiticeiro:
    def __init__(self, nome):
        self._nome = nome
        self._encantamento = None
        
    def atacar(self):
        if self._encantamento is not None:
            print(f"{self._nome} lança seu feitiço e causa (13) ponto(s) de dano.")
        else:
            print(f"{self._nome} ataca com as mãos e causa (1) ponto de dano.")
        
class GrupoAventureiros:
    def __init__(self, nome):
        self._nome = nome
        self._guerreiro = None
        self._feiticeiro = None

#Driver Code
guerreiro_1 = Guerreiro("Átila, o Huno")
guerreiro_1.atacar()

feiticeiro_1 = Feiticeiro("Gandalf, o Brando")
feiticeiro_1.atacar()

guerreiro_1._arma = True
feiticeiro_1._encantamento = True

guerreiro_1.atacar()
feiticeiro_1.atacar()

#Nas linhas anteriores, guerreiro e feiticeiro não tinham exatamente NENHUMA
# associação, a partir daqui, guerreiro e feiticeiro estão fracamente 
# associados, e (grupo - feiticeiro) e (grupo - guerreiro) estão agregados.
#Na associação, não há dependência, eles se encontram no código mas não são
# dependentes um do outro. 

grupo_dos_sonhos = GrupoAventureiros("grupo dos sonhos")
grupo_dos_sonhos._guerreiro = guerreiro_1
grupo_dos_sonhos._feiticeiro = feiticeiro_1
print(grupo_dos_sonhos)
