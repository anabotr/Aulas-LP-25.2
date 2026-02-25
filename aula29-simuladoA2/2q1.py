from datetime import datetime

class Livro:
    def __init__(self, titulo, autor, genero, estado, owner):
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        self._estado = estado
        self._owner = owner
    
    def titulo(self):
        return self._titulo
    
    def autor(self):
        return self._autor
    
    def genero(self):
        return self._genero
    
    def estado(self):
        return self._estado
    
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, name):
        self._owner = name

class Transacao:
    def __init__(self, livro_1, livro_2):
        self._l1 = livro_1
        self._l2 = livro_2
        self._status = "Pendente"
        self._data = None
    
    def l1(self):
        return self._l1
    
    def l2(self):
        return self._l2
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, msg):
        self._status = msg
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, data):
        self._data = data
    
    def realiza_troca(self):
        self.data = datetime.now()
        self.status = "Concluída"
        ow_l2 = self.l2().owner
        self.l1().owner = self.l2().owner
        self.l2().owner = ow_l2

    def recusa_troca(self):
        self.data = datetime.now()
        self.status = "Cancelada"



class Usuario:
    def __init__(self, nome):
        self._nome = nome
        self._anuncios = [""]
        self._trocas = [""]
        self._rating = 0

    @property
    def nome(self):
        return self._nome
    
    @property
    def anuncios(self):
        return self._anuncios
    
    def add_anuncio(self, livro):
        self.anuncios.append(livro)

    def rm_anuncio(self, livro):
        self.anuncios.remove(livro)
    
    @property
    def trocas(self):
        return self._trocas
    
    def add_troca(self, troca):
        self.trocas.append(troca)
    
    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, valor):
        self._rating = (self._rating*(len(self.trocas) - 1) + valor)/(len(self.trocas)-1)

    def anunciar_livro(self, livro: Livro):
        print(f"{self.nome} anunciou {livro.titulo()}!")
        self.add_anuncio(livro)

    def solicitar_troca(self, troca):
        self.add_troca(troca)
        troca.l2().owner.add_troca(troca)

    def responder_troca(self, troca, resposta):
        if resposta == "Concluída":
            self.rm_anuncio(troca.l2())
            troca.l1().owner.rm_anuncio(troca.l1())
            troca.realiza_troca()
        else:
            troca.recusa_troca()

    def avaliar_usuario(self, usuario, nota):
        usuario.rating = nota


###########################################################
#Driver Code

ana = Usuario("Ana")
larissa = Usuario("Larissa")

morro = Livro("O morro dos ventos uivantes", "Bronte", "Romance", "Novo", ana)
aia = Livro("O conto de aia", "Esqueci", "livri", "Bom", ana)
cubas = Livro("Memórias Póstumas de Brás Cubas", "Machadão", "Romance", "Gasto", larissa)
After = Livro("After", "sla", "Fanfic", "novo", larissa)

ana.anunciar_livro(morro)
ana.anunciar_livro(cubas)
larissa.anunciar_livro(aia)
larissa.anunciar_livro(After)

print(ana.anuncios)
print(larissa.anuncios)

t1 = Transacao(morro, aia)
t2 = Transacao(After, cubas)

ana.solicitar_troca(t1)
larissa.solicitar_troca(t2)

print(ana.trocas)
print(larissa.trocas)

larissa.responder_troca(t1, "Concluída")
larissa.avaliar_usuario(ana, 4)
ana.avaliar_usuario(larissa, 5)

print(ana.rating)
print(larissa.rating)
print(ana.trocas)
print(larissa.trocas)

ana.responder_troca(t2, "Cancelada")
ana.avaliar_usuario(larissa, 0)
larissa.avaliar_usuario(ana, 3)


print(ana.rating)
print(larissa.rating)
print(ana.trocas)
print(larissa.trocas)


print(ana.anuncios)
print(larissa.anuncios)

