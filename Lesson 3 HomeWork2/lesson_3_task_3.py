from mailing import Mailing
from address import Address

# to_address = Address(426000, "Izhevsk,", "Karla Marksa st.,", 215, 17)
# from_address = Address(437528, "Moscow,", "Valovaya st.,", 26, 5)

def sayMailing(self):
    print("Отправление", self.track, "из", self.from_address, "в", self.to_address,".", "Стоимость", self.cost, "рублей.")

newMail = Mailing(Address(426000, "Izhevsk,", "Karla Marksa st.,", 215, 17), Address(437528, "Moscow,", "Valovaya st.,", 26, 5), 1999, '999888777')
newMail.sayMailing()