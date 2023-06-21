def is_year_leap():
    n = input("Введите год: ")
    if(int(n) % 4 == 0):
        print("год", n+":", True)
    else:
        print("год", n+":", False)
is_year_leap()

