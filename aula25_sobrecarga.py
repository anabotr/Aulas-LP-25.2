"""
Alguns operadores que podem ser sobrecarregados (tem outro significado dentro
                                                 da nossa classe):
_______________________________________________________________________________

__lt__: lesser than
__le__: lesser qual
__gt__: greather than
__ge__: greather equal
__eq__: equal
__ne__ : not equal
__add__: addition
__sub__: subtraction
__mul__: multiplication
__floordiv__ : floor of division
__truediv__: divisão de ponto flutuante
__neg(other)__: negative

e muitos mais!
_______________________________________________________________________________
"""

#Há dois tipos de sobrecarga: de operadores ou de métodos herdados

class Aluno:
    def __init__(self, qi, n_artigos_publicados):
        self.qi = qi
        self.n_ap = n_artigos_publicados
        
    def __str__(self):
        return f"QI: {self.qi} e Publicações: {self.n_ap}"
    
    def __add__(self, other): #Aqui, estamos definindo a soma entre objetos, 
    # porque o python no sabe como fazer isso se não dissermos como
        qi_total = self.qi + other.qi - 100 #somamos as diferenças para 100 de 
        # cada aluno + 100
        publicacos_acum = self.n_ap + other.n_ap
        return Aluno(qi_total, publicacos_acum)
        
    def __gt__(self, other): #definindo o operador >, deve retornar True/False
        if self.qi > other.qi:
            return True
        elif self.qi == other.qi:
            return self.n_ap > other.n_ap
        else:
            return False
    
aluno_1 = Aluno(114, 0)
aluno_2 = Aluno(120, 2)
super_aluno = aluno_1 + aluno_2 #o python vê: aluno_1.add(aluno_2)
print(aluno_1)
print(aluno_2)
print(super_aluno)

if aluno_1 > aluno_2:
    print("Selecionar aluno 1")
else:
    print("Selecionar aluno 2")