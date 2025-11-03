class Cachorro:
    """
    Classe que representa um cachorro.
    """
    
    contador_cachorros = 0 #isso é um atributo de classe, vai ser compartilhado
    # entre todos os objetos da classe
    
    def __init__(self, nome, raca, idade):
        '''
        docstring lindo

        Parameters
        ----------
        nome : TYPE
            DESCRIPTION.
        raca : TYPE
            DESCRIPTION.
        idade : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        '''
        #o init inicializa um objeto que já existe e o modifica com os 
        # parametros passados
        
        self.nome = nome #se o atributo nome não existe, ele é criado.
        self.raca = raca
        self.idade = idade
        Cachorro.contador_cachorros += 1 
    
    def latir(self):
        return "Au Au!"
    
    @classmethod #isso faz com que usemos as variáveis de escopo da classe do 
    # objeto dado
    def get_numero_cachorros(cls):
        return cls.contador_cachorros
    
    @classmethod
    def from_String(cls, string_cachorro):
        """Vai criar e inicializar um cachorro a parit de um texto
        """
        nome, raca, idade = string_cachorro.split(",")
        return cls(nome, raca, idade)
    
    
cachorro_1 = Cachorro("Cacau", "Lulu", "7")
cachorro_2 = Cachorro("Pepe", "Labrador", "18")

print(Cachorro.get_numero_cachorros())
#print(Cachorro.contador_cachorros) também funciona, porque não está protegido
print(cachorro_1.latir())

cachorro_3 = Cachorro.from_String("Jade,Golden,5")
print(Cachorro.get_numero_cachorros())
print(cachorro_3.latir())

