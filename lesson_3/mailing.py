from adress import Adress

class Mailing:
    to_adress = Adress
    from_adress = Adress
    cost  = int
    track = str
    
    def __init__(self, to_adress, from_adress, cost, track):
        self.to_adress = to_adress
        self.from_adress = from_adress
        self.cost = cost
        self.track = track
        
    def printMailing(self):
        print(f'Отправление {self.track} из {self.to_adress} в {self.from_adress}. Стоимость {self.cost} рублей.')