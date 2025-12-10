#### Questão 2 - implementação e uso

import random
from datetime import datetime, timedelta

class RoomDatabase:
    rooms = [("standard", 200), ("deluxe", 350), ("suite", 600)]
    discounts = {"standard": 0.05, "suite": 0.1}
    def get_available_rooms(self, start: datetime, end: datetime) -> list:
        print(f"Buscando quartos disponíveis entre {start} e {end}...")
        idx = random.randint(0+1, len(self.__class__.rooms))
        return self.__class__.rooms[:idx]


    def get_discounts(self) -> list:
        print("Buscando descontos aplicáveis...")
        return self.__class__.discounts

class User:
    def __init__(self, name: str, email: str, phone: int, user_is_vip: bool = False):
        self.name = name
        self.email = email
        self.phone = phone
        self.user_is_vip = user_is_vip

class ReservationPreferences:
    def __init__(self, prefer_suite: bool = False, breakfast: bool = False):
        self.prefer_suite = prefer_suite
        self.breakfast = breakfast

class Notificacoes:
    def __init__(self, user: User):
        self.user = user
    
    def notify(self, msg: str) -> None:
        self.send_email(msg)
        self.send_sms(msg)
    
    def send_email(self, msg: str) -> str:
        return f"Enviando email para {self.user.email}: {msg}"

    def send_sms(self, msg: str) -> str:
        return f"Enviando sms para {self.user.phone}: {msg}"


class ReservationSystem:
    db = RoomDatabase()
    def __init__(self, user: User, start: datetime, end: datetime, preferences: ReservationPreferences, notificacoes: Notificacoes):
        self.user = user
        self.start = start
        self.end = end
        self.preferences = preferences
        self.notificacoes = notificacoes
    
    def available_rooms(self) -> list:
        rooms = self.__class__.db.get_available_rooms(self.start, self.end)
        return rooms
    
    def available_discounts(self) -> list:
        discounts = self.__class__.db.get_discounts()
        return discounts
    
    def generate_possibilities(self, rooms: list, discounts: list) -> list:
        possibilities = []
        for (rtype, base_price) in rooms:
            price = base_price
            if self.preferences.breakfast:
                price += 35

            if self.user.user_is_vip and (rtype in discounts):
                price = price * (1 - discounts[rtype])

            possibilities.append((rtype, price))
        return possibilities
    
    def sort_possibilites(self, possibilities: list) -> list:
        if self.preferences.prefer_suite:
            possibilities.sort(key=lambda x: 0 if x[0] == "suite" else 1)
        else:
            possibilities.sort(key=lambda x: x[1])
        return possibilities

    def log_reservation(self, chosen: tuple) -> None:
        with open("reservas.log", "a") as f:
            f.write(f"{self.user}:{chosen}:{self.start}->{self.end}\n")

    def reserve(self) -> tuple:
        rooms = self.available_rooms()
        discounts = self.available_discounts()
        possibilities = self.generate_possibilities(rooms, discounts)
        final = self.sort_possibilites(possibilities)
        chosen = final[0]

        self.log_reservation(chosen)
        msg = f"Reserva confirmada para o quarto {chosen[0]} no valor de {chosen[1]:.2f}"
        self.notificacoes.notify(msg)
        return chosen
        

def main():
    user = User("carla", "carla@cliente.com", 99999999, True)
    start = datetime.now()
    end = start + timedelta(days=3) # Operação entre datas
    pref = ReservationPreferences(True, True)
    notif = Notificacoes(user)
    rs = ReservationSystem(user, start, end, pref, notif)
    reserva = rs.reserve()
    print(reserva)

if __name__ == "__main__":
    main()