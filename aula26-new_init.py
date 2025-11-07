class EMAp:
    def __new__(cls, *args, **kwargs): #O new olha para a instância de uma 
       # classe
       #Estamos controlandoo "momento de concepção" de um objeto, o new chama
       # quem cria o objeto
       
       #A lógica é: faço o que é só do meu new e chamo o new do meu pai, e isso 
       # segue em cadeia até que seja chamado o new de object (todos precisam 
       # ser objetos)
       
       print("Podemos fazer o que quisermos antes da instância ser criada")
       object_ = super().__new__(cls)
       print("Podemos fazer o que quisermos depois da instância ser criada")
       #A gente pode "se meter" no fluxo da linguagem
       return object_
   
    def __init__(self, n_alunos):
        print("Podemos fazer o que quisermos antes da instância ser inicializada")
        self.n_alunos = n_alunos
        print("Podemos fazer o que quisermos depois da instância ser inicializada")
        
escola_nutella = EMAp((42)) #Esse é o jeito "molezinha" de fazer um objeto, 
#porque aqui, o python desencadeia várias chamadas por você, como chamar o new
print(escola_nutella.n_alunos)

print("_"*60)

#Aqui, estamos fazendo do jeito mais manual
escola_raiz = object.__new__(EMAp)
escola_raiz.__init__(666)
print(escola_raiz.n_alunos)

#HACK: O new CRIA, o init INICIALIZA os objetos!!!