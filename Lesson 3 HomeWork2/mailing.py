from address import Address

class Mailing:

    to_address = Address()
    from_address = Address()
    cost = 0
    track = ''

    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track
    # def sayMailing(self):
    #     print("Отправление", self.track, "из", self.from_address, "в", self.to_address,".", "Стоимость", self.cost, "рублей.")
