class Address:

    index = 000000
    city = ''
    street = ''
    house = 0
    apartment = 0

    def __init__(self, index, city, street, house, apartment):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment
    def sayAddress(self):
        print(self.index, self.city, self.street, self.house,"-",self.apartment)