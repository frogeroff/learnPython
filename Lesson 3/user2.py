class User:

    age = 0
    name = 'No Name'
    email = 'mail@test.ru'

    def __init__(self, _name, _age, _email):
        self.age = _age
        self.name = _name
        self.email = _email

    def sayName (self):
        print (self.name)

    def sayEmail(self):
        print (self.email)

newUser = User('Alex', 29, 'hello_alex@mail.ru')
newUser.sayName () # Выведет Alex
newUser.sayEmail() # Выведет hello_alex@maii.ru