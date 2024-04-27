class Adress:
    index = int
    town = str
    street = str
    house = int
    flat = int
    fulladress = str
    
    def __init__(self, index, town, street, house, flat):
        self.index = index
        self.town = town
        self.street = street
        self.house = house
        self.flat = flat
        self.fulladress = f'{self.index}, {self.town}, {self.street}, {self.house} - {self.flat}'       