class Guerreiro:
    def __init__(self, nome):
        self._nome = nome
        self._arma = None
        
    def atacar(self):
        if self._arma is not None:
            print(f"{self._nome} ataca com {self._arma._nome} e causa ({self._arma._dano}) ponto(s) de dano.")
            #o código da classe guerreiro tem que conhecer o código da classe 
            #arma porque usa arma._nome
            #Aumentamos o acoplamento entre as classes, quanto mais o 
            #acoplamento aumenta, pior é para resolver os bugs -> ISSO É UM 
            #PROBLEMA!!!!!!!!!!!!
        else:
            print(f"{self._nome} ataca com as mãos e causa (1) ponto de dano.")
    
    #No meu programa, meu objeto do tipo guerreiro tem um espaço no qual ele 
    #pode fazer a referência a um outro objeto do tipo arma
    
class Arma1M:   
    """arma de uma mao"""
    def __init__(self, nome, dano):
        self._nome = nome
        self._dano = dano
    
    #vamos configurar o print, pq arma1m herdou de sua família mas não gostamos
    #de como está e queremos mudar o dunder method
    #o __str__ é o que é chamado quando pedimos print(arma = Arma1M(nome, dano))
    def __str__(self):
        return f"A arma \"{self._nome}\" causa ({self._dano}) ponto(s) de dano"

#Os objetos são independentes nesse caso: um vive sem o outro, mas a ideia de 
#agregação é fazer com que os objetos sejam independentes: se um objeto morre,
#ninguém depende dele então todo mundo continua ok
#Os objetos se relacionam mas não são dependentes!
        
#Driver Code
guerreiro_1 = Guerreiro("Vercingetorix")
guerreiro_1.atacar()

guerreiro_2 = Guerreiro("Boudicca")
guerreiro_2.atacar()

arma_1 = Arma1M("Adaga", 7)   
print(arma_1) 
    
arma_2 = Arma1M("Espada Curta", 13)
print(arma_2)

guerreiro_1._arma = arma_1
guerreiro_2._arma = arma_2

guerreiro_1.atacar()
guerreiro_2.atacar()  

del arma_1

guerreiro_1.atacar()

del guerreiro_1
del guerreiro_2

#print(arma_1)
print(arma_2)

#perceba que se os guerreiros não existirem, as armas continuam existindo (a
#volta foi mostrada no início do driver code), ou seja, os objetos não são
#dependentes entre si


#Mas se apagarmos a arma sem apagar o guerreiro?
