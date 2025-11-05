class Foo:
    def __init__(self):
        self.public = "Public" #a mensagem desse atributo é que ele pode ser
        # modificado a vontade através da instância
        self._protected = "Protected" #a mensagem desse é que ele não deve ser 
        # acessado, mas, se alguém quiser, é facil fazê-lo. Todas as classes 
        # filhas de foo herdam esse atributo.
        self.__private = "Private" #também consegue ser acessado, mas tem um 
        # grau a mais de dificuldade. Este não é herdado pelas classes filhas.
        
    def public_method(self):
        print("Olá, eu sou o método público") #Por ser público, esse método 
        # consegue olhar e chamar outros métodos da mesma classe
        self._protected_method() #Publico consegue chamar ambos os métodos 
        # porque ele os ve
        self.__private_method()
        
    def _protected_method(self):
        print("Olá, eu sou o método protegido") #Esse método deveria poder ser 
        # chamado apenas por essa classe e seus filhos, ninguém de fora
        self.__private_method()
        #Esse método também consegue acessar o público, mas todo mundo consegue
        
    def __private_method(self):
        print("Olá, eu sou o método privado") #Esse método deveria poder ser 
        # chamado exclusivamente por essa classe.
        
class Bar(Foo):
    def usando_os_metodos_do_papai(self):
        super()._protected_method()
        super()._Foo__private_method() #Erro semântico: não deveria ser 
        # possível acessar um métodos privado a partir do filho
        

object_ = Foo()
print(object_.public)
object_.public_method()

#ERRO SEMÂNTICO: eu digo que é protegido mas usam como público, porque o python
# deixa
print(object_._protected) #a gente não deveria conseguir fazer isso, mas 
# conseguimos porque o python funciona assim
object_._protected_method()

#ERRO SEMÂNTICO ** 2: eu digo que é protegido mas usam como público, porque o 
# python deixa
print(object_._Foo__private) #o python dificulta um pouco o acesso para obrigar 
# a outra pessoa a ver que ela está fazendo algo que não deveria
#para acessar, precisamos usar o nome completo de um atributo:
# _classatribute
object_._Foo__private_method()



object2_ = Bar()
print(object2_.public)
object2_.public_method()

object2_.usando_os_metodos_do_papai() #isso não é erro semântico porque eu 
# escolho como e quando o nosso objeto de bar pode usar os métodos de foo. 
#Controlamos o que é de dentro mostrando apenas o que queremos. Essa é a ideia 
# do getter e do setter

#ERRO SEMÂNTICO
print(object2_._protected)
object2_._protected_method()

#ERRO SEMÂNTICO**2
print(object2_._Foo__private)
object2_._Foo__private_method()