class Fruta:
    def __init__(self, nome):
        self.nome = nome

    def envelhecer_na_despensa(self):
        print(f"{self.nome} está envelhecendo na despensa.")

banana = Fruta("banana")

banana.envelhecer_na_despensa() #isso é equivalente a 
# Fruta.envelhecer_na_despensa("banana"), que é o jeito "raiz"

print("_"*40)

maca = Fruta("maca")
print(maca.__dict__) #o init coloca o que você passa no dicionário do objeto
print(vars(maca)) #outra forma de ver a mesma coisa
print("_"*40)

maca.peso = 1 #funciona pq é como se colocássemos manualmente no dicionário, 
# porém, as outras frutas não terão esses mesmos atributos
maca.validade = "31/12/2025"
print(maca.nome)
print(maca.peso)
print(maca.validade)

del maca.__dict__["peso"]
del maca.__dict__["validade"]
print(maca.__dict__)

maca.__dict__["tipo"] = "Gala"
print(maca.__dict__)