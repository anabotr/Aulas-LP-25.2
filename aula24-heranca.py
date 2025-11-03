class Animal:
    def __init__(self, nome, especie):
        '''docstring lindo'''
        self.nome = nome
        self.especie = especie
        
    def morrer(self):
        return f"{self.nome} morreu"
    
    def __str__(self): #sobrecarregar é criar um método que já existe
        return f"{self.nome} é da espécie {self.especie}"
        

class Cachorro(Animal):
    #se eu não colocar um init ou morrer em cachorro, ele chamará as funções
    # de animal. Se não houver código aqui, ele terá nome, espécie e morrerá.
    def __init__(self, nome, raca):
        super().__init__(nome, especie = "cachorro") #o super invoca o pai
        self.raca = raca
        
    def morrer(self): #se isso não fosse criado, cachorro.morrer() chamaria
    # morrer de Animal, porém, fazendo isso, sobrescrevemos a função
        return f"{self.nome} foi para a fazenda, onde viverá feliz para sempre"
    
    def __repr__(self):
        class_ = type(self).__name__
        return (f"{class_} (nome = {self.nome!r}), "
                f"(raca = {self.raca!r}), "
                f"(especie = {self.especie!r})")
        #sempre que estamos dentro de uma representação de um objeto imprimindo
        # outros objetos (self.raca, self.nome, ...) usamos sua representação 
        # por meio do !r
        #o string é PARA O USUÁRIO LER, internamente, o python trabalha com a 
        # representação entre os programas
    
    def latir(self):
        return f"{self.nome} está latindo"
    
    def __str__(self):
        return f"{self.nome} é um(a) {self.raca}"
    

class Gato(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, especie = "gato")
        self.raca = raca
        
    def morrer(self):
        return f"{self.nome} tem 7 vidas!"
    
    def miar(self):
        return f"{self.nome} está miando"
    
        
cachorro_1 = Cachorro("Au Au", "Vira-lata")
print(cachorro_1)
print(cachorro_1.morrer())
print(cachorro_1.latir())
print("_"*60)

gato_1 = Gato("Miau", "Vira_Lata")
print(str(gato_1))
print(gato_1.miar())
print(gato_1.morrer())
print(f"{gato_1!s}") #o !s roda o método string do objeto passado na fstring
print("_"*60)

print(ascii(gato_1))
print(f"{gato_1!a}") #era para rodar o método ascii, e ele sempre chama o 
# método reprsentação, que, se não formatado, imprime aquele <__main__ papapa>
#o método string faz a mesma coisa

print(ascii(cachorro_1))
print(f"{cachorro_1!a}")
print(str(cachorro_1))
