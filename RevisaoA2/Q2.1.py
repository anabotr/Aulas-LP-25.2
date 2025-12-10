#### Questão 2 - identificação de erros

import random
from datetime import datetime, timedelta

class RoomDatabase:
    def get_available_rooms(self, start, end):
        #Aqui, o OCP é desrespeitado, porque não é possível extender/reduzir a lista de quartos sem 
        # modificar a classe
        print(f"Buscando quartos disponíveis entre {start} e {end}...")
        base = [("standard", 200), ("deluxe", 350), ("suite", 600)]
        # remove aleatoriamente um para simular ocupação
        if random.random() < 0.5:
            base.pop(0)
        return base

    def get_discounts(self):
        print("Buscando descontos aplicáveis...")
        return {"standard": 0.05, "suite": 0.1}

class ReservationSystem:
    #Aqui, o SRP está sendo quebrado, pois uma mesma função faz tudo: calcula a reserva, o preço, 
    # cria arquivos, envia feedbacks
    #Isso acaba quebrando também o OCP, porque é muito difícil extender essa classe sem ter que
    # mudá-la
    #uma sugestão é criar uma classe para preferências do cliente e uma para as notificações
    def reserve(
        self,
        user,
        start,
        end,
        user_is_vip=False,
        prefer_suite=False,
        include_breakfast=False,
        notify_email=True,
        notify_sms=False
    ):
        db = RoomDatabase()

        # coletar quartos disponíveis
        rooms = db.get_available_rooms(start, end)

        # aplicar discounts
        discounts = db.get_discounts()
        final = []
        for (rtype, base_price) in rooms:
            price = base_price

            if include_breakfast:
                price += 35

            if user_is_vip and rtype in discounts:
                price = price * (1 - discounts[rtype])

            final.append((rtype, price))

        # preferências do usuário
        if prefer_suite:
            final.sort(key=lambda x: 0 if x[0] == "suite" else 1)
        else:
            final.sort(key=lambda x: x[1])

        chosen = final[0]

        # simula persistência
        with open("reservas.log", "a") as f:
            f.write(f"{user}:{chosen}:{start}->{end}\n")

        # enviar notificações
        msg = f"Reserva confirmada para o quarto {chosen[0]} no valor de {chosen[1]:.2f}"
        if notify_email:
            print(f"Enviando email para {user}: {msg}")
        if notify_sms:
            print(f"Enviando SMS para {user}: {msg}")

        return chosen
        

def main():
    user = "carla@cliente.com"
    start = datetime.now()
    end = start + timedelta(days=3) # Operação entre datas

    rs = ReservationSystem()
    reserva = rs.reserve(
        user, start, end,
        user_is_vip=True,                  # agora precisa desse flag
        prefer_suite=True,
        include_breakfast=True
    )
    print(reserva)