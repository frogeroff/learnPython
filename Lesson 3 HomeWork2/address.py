class Address:
    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment
    def sayAddress(self):
        print(self.index, self.city, self.street, self.house,"-",self.apartment)

addressTo = Address("426000,", "Izhevsk,", "Karla Marksa st.,", "215", "17")
addressTo.sayAddress()

addressFrom = Address("437528,", "Moscow,", "Valovaya st.,", "26", "5")
addressFrom.sayAddress()
