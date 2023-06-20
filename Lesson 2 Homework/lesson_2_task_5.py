month_to_season = input("Номер месяца: ")
x = int(month_to_season)

month_name = ""
if x in range(1, 3):
    print("Месяц: Зима")
elif x in range(3, 6):
    print("Месяц: Весна")
elif x in range(6, 9):
    print("Месяц: Лето")
elif x in range(9, 12):
    print("Месяц: Осень")
elif x == 12:
    print("Месяц: Зима")
else:
    print("Введите номер месяца от 1 до 12")
