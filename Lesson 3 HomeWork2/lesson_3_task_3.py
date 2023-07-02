from mailing import Mailing
from address import Address

def sayMailing(self):
    print("Отправление", self.track, "из", self.from_address, "в", self.to_address,".", "Стоимость", self.cost, "рублей.")
        
to_address = Address("426000,", "Izhevsk,", "Karla Marksa st.,", "215,", "17")
# to_address.sayAddress()
from_address = Address("437528,", "Moscow,", "Valovaya st.,", "26,", "5")
# from_address.sayAddress()
post = Mailing(to_address, from_address, 1000, "77777777")
post.sayMailing()