
n = input("Введите год: ")
if(int(n) % 4 == 0):
    print(True)
else:
    print(False)

def is_year_leap(year):
    print("год", year,":")
is_year_leap(n)
