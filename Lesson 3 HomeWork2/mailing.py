from address import Address

# addressTo = Address("426000,", "Izhevsk,", "Karla Marksa st.,", "215", "17")
# addressTo.sayAddress()

# addressFrom = Address("437528,", "Moscow,", "Valovaya st.,", "26", "5")
# addressFrom.sayAddress()

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = Address(to_address)
        self.from_address = Address(from_address)
        self.cost = int(cost)
        self.track = str(track)
    def sayMailing(self):
        print("Отправление", self.track, "из", self.from_address, "в", self.to_address,".", "Стоимость", self.cost, "рублей.")

# mailing_1 = Mailing(to_address, from_address, 1000, "77777777")
# mailing_1.sayMailing()
