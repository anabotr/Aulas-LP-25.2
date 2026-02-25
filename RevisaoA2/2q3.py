class LeagueManagerError(Exception): pass
class PartidaNaoRealizadaError(LeagueManagerError): pass

class Time:
    def __init__(self, nome):
        self._nome = nome
        self._pontuacao = 0
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def pontuacao(self):
        return self._pontuacao
    
    @pontuacao.setter
    def pontuacao(self, amount):
        self._pontuacao = amount


class Partida:
    def __init__(self, time_1, time_2): 
        self._time_1 = time_1
        self._time_2 = time_2
        self._placar = None
        self._vencedor = None
    
    @property
    def time_1(self):
        return self._time_1
    
    @property
    def time_2(self):
        return self._time_2
    
    @property
    def placar(self):
        return self._placar
    
    @placar.setter
    def placar(self, placar: tuple):
        self._placar = placar
    
    @property
    def vencedor(self):
        return self._vencedor
    
    @vencedor.setter
    def vencedor(self, vencedor):
        self._vencedor = vencedor
    
    def define_vencedor(self):
        if self.placar is not None:
            if self.placar[0] > self.placar[1]:
                return self.time_1
            elif self.placar[0] == self.placar[1]:
                return None
            else:
                return self.time_2
        else:
            raise PartidaNaoRealizadaError
    
    def atualiza_partida(self, placar: tuple):
        self.placar = placar
        self.vencedor = self.define_vencedor()
        self.atualiza_times()
    
    def atualiza_times(self):
        if self.vencedor is not None:
            if self.vencedor == self.time_1:
                self.atualiza_pontos(self.time_1, 3)
            else:
                self.atualiza_pontos(self.time_2, 3)
        else:
            self.atualiza_pontos(self.time_1, 1)
            self.atualiza_pontos(self.time_2, 1)

    def atualiza_pontos(self, time: Time, pontos: int):
        time.pontuacao += pontos
        


class Torneio:
    def __init__(self, nome): 
        self._nome = nome
        self._times = []
        self._partidas = []
        self._resultados = {}
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def times(self):
        return self._times
    
    @property
    def partidas(self):
        return self._partidas
    
    def add_partida(self, partida: Partida):
        self.partidas.append(partida)
    
    def indice_partida(self, partida: Partida):
        return self.partidas.index(partida)

    @property
    def resultados(self):
        return self._resultados

    def add_time(self, time):
        self.times.append(time)
    
    def rm_time(self,time):
        self.times.remove(time)

    def gera_partidas(self): 
        for i1, time1 in enumerate(self.times):
            for i2, time2 in enumerate(self.times):
                if i1 > i2:
                    self.add_partida(Partida(time1, time2))

    def registra_resultado(self, partida: Partida, resultado: tuple): 
        partida.atualiza_partida(resultado)
        self.resultados[partida] = partida.vencedor


flamengo = Time("flamengo")
vasco = Time("vasco")
fluminense = Time("fluminense")
botafogo = Time("botafogo")

torneio = Torneio("torneio")

torneio.add_time(flamengo)
torneio.add_time(fluminense)
torneio.add_time(vasco)
torneio.add_time(botafogo)

torneio.gera_partidas()

torneio.registra_resultado(torneio.partidas[0], (2,1))
print(torneio.partidas[0].time_1.nome)
print(torneio.partidas[0].time_2.nome)
print("------")

torneio.registra_resultado(torneio.partidas[1], (0,0))
print(torneio.partidas[1].time_1.nome)
print(torneio.partidas[1].time_2.nome)
print("------")

torneio.registra_resultado(torneio.partidas[2], (3,5))
print(torneio.partidas[2].time_1.nome)
print(torneio.partidas[2].time_2.nome)
print("------")

torneio.registra_resultado(torneio.partidas[3], (2,2))
print(torneio.partidas[3].time_1.nome)
print(torneio.partidas[3].time_2.nome)
print("------")

torneio.registra_resultado(torneio.partidas[4], (7,1))
print(torneio.partidas[4].time_1.nome)
print(torneio.partidas[4].time_2.nome)
print("------")

torneio.registra_resultado(torneio.partidas[5], (0,3))
print(torneio.partidas[5].time_1.nome)
print(torneio.partidas[5].time_2.nome)
print("------")

print(flamengo.pontuacao)
print(fluminense.pontuacao)
print(botafogo.pontuacao)
print(vasco.pontuacao)

