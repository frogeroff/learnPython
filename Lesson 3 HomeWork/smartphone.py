class Smartphone:
    def __init__(self, _marka, _model, _number):
        self.marka = _marka
        self.model = _model
        self.number = _number
    def sayMarka(self):
        print()
        print("Марка телефона:", self.marka)
    def sayModel(self):
        print("Модель телефона:", self.model)
    def sayNumber(self):
        print("Абонентский номер:", self.number)

A = Smartphone("Samsung", "S23", "+79991234567")
A.sayMarka()
A.sayModel()
A.sayNumber()

B = Smartphone("Apple", "iPhone 14 Pro", "+79998887766")
B.sayMarka()
B.sayModel()
B.sayNumber()

C = Smartphone("Xiaomi", "13 Lite", "+79992223355")
C.sayMarka()
C.sayModel()
C.sayNumber()

D = Smartphone("Honor", "X7", "+79991114447898")
D.sayMarka()
D.sayModel()
D.sayNumber()

E = Smartphone("Huawei", "Y7 Lite", "+79995554466")
E.sayMarka()
E.sayModel()
E.sayNumber()

catalog = [A, B, C, D, E]
for i in range(0, -1):
    print(catalog[i])