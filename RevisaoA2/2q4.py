class Error(Exception): pass

class SessaoNotFoundError(Error): pass

class Habilidade:
    def __init__(self, nome: str, proficiencia: str, descrição: str): 
        self._nome = nome
        self._proficiencia = proficiencia
        self._descricao = descrição
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def proficiencia(self):
        return self._proficiencia
    
    @property
    def descricao(self):
        return self._descricao

class Sessão:
    def __init__(self, mentor, aprendiz, habilidade_ensinada: Habilidade, duração_prevista:str): 
        self._mentor = mentor
        self._aprendiz = aprendiz
        self._habilidade = habilidade_ensinada
        self._duracao = duração_prevista
        self._status = "Agendada"
        self.autoadd()
    
    @property
    def mentor(self):
        return self._mentor
    
    @property
    def aprendiz(self):
        return self._aprendiz
    
    @property
    def habilidade(self):
        return self._habilidade
    
    @property
    def duracao(self):
        return self._duracao
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, status):
        self._status = status
    
    def verifica_sessao(self, membro):
        return membro.tem_sessao(self)

    def autoadd(self):
        if not self.verifica_sessao(self.mentor):
            self.mentor.add_sessao(self)
        if not self.verifica_sessao(self.aprendiz):
            self.aprendiz.add_sessao(self)

    def cancela(self):
        self.status = "Cancelada"
    
    def realiza(self):
        self.status = "Realizada"



class Membro:
    def __init__(self, nome: str): 
        self._nome = nome
        self._habilidades = []
        self._sessoes = []
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def habilidades(self):
        return self._habilidades
    
    def add_habilidade(self, habilidade):
        self.habilidades.append(habilidade)
    
    def rm_habilidade(self, habilidade):
        self.habilidades.remove(habilidade)
    
    @property
    def sessoes(self):
        return self._sessoes
    
    def add_sessao(self, sessao):
        self.sessoes.append(sessao)
    
    def rm_sessao(self, sessao):
        self.sessoes.remove(sessao)
    
    def tem_sessao(self, sessao):
        return sessao in self.sessoes

    def solicita_sessão(self, mentor, aprendiz, habilidade_ensinada: Habilidade, duração_prevista:str):
        return Sessão(mentor, aprendiz, habilidade_ensinada, duração_prevista)
    
    def cancela_sessao(self, sessao):
        if self.tem_sessao(sessao):
            sessao.cancela()
        else:
            raise SessaoNotFoundError
    
    def realiza_sessao(self, sessao):
        if self.tem_sessao(sessao):
            sessao.realiza()
        else:
            raise SessaoNotFoundError
        
ana = Membro("Ana")
larissa = Membro("Larissa")

croche = Habilidade("crochê", "médio", "crochê de roupas e peças de casa")
ingles = Habilidade("inglês", "alto", "i speko")

ana.add_habilidade(croche)
larissa.add_habilidade(ingles)

print(ana.habilidades)
print(larissa.habilidades)
print(ana.sessoes)
print(larissa.sessoes)

aula1 = ana.solicita_sessão(larissa, ana, ingles, "1h")
aula2 = larissa.solicita_sessão(ana, larissa, croche, "3h")

print(aula1.status)
print(aula2.status)
print(ana.sessoes)
print(larissa.sessoes)

ana.cancela_sessao(aula2)
larissa.realiza_sessao(aula1)

print(aula1.status)
print(aula2.status)
print(ana.sessoes)
print(larissa.sessoes)