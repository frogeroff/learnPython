class Smartphone:
    def __init__(self, _marka, _model, _number):
        self.marka = _marka
        self.model = _model
        self.number = _number
    def saySmartphone(self):
        print(self.marka,"-",self.model,"-",self.number)

A = Smartphone("Samsung", "S23", "+79991234567")
A.saySmartphone()

B = Smartphone("Apple", "iPhone 14 Pro", "+79998887766")
B.saySmartphone()

C = Smartphone("Xiaomi", "13 Lite", "+79992223355")
C.saySmartphone()

D = Smartphone("Honor", "X7", "+79991114447898")
D.saySmartphone()

E = Smartphone("Huawei", "Y7 Lite", "+79995554466")
E.saySmartphone()