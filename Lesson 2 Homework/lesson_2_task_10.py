def bank():
    X = int(input("Введите начальную сумму: ")) #Размер вклада
    Y = int(input("Укажите срок вклада: ")) #Срок вклада
    S = 0.1 #Годовая ставка
    if(Y < 1):
        print("Минимальный срок вклада 1 год")
        return
    if(Y > 10):
        print("Максимальный срок вклада 10 лет")
        return
    profit = round(X*(1 + S)**Y, 2)

    print("К концу вклада у вас будет", profit)
bank()