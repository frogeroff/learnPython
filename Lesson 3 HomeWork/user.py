class User:
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.surname = last_name
    def sayName(self):
        print("Мое имя: ", self.name)
    def saySurname(self):
        print("Моя фамилия: ", self.surname)
    def sayAll(self):
        print("Мои имя и фамилия: ", self.name, self.surname)
X = User("Александр", "Кожевников")
X.sayName()
X.saySurname()
X.sayAll()