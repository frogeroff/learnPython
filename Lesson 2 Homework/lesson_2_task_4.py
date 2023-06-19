fizz_buzz = input("Введите число: ")
n = int(fizz_buzz)
for fizz_buzz in range(1, n):
    if(fizz_buzz % 3 == 0):
        print("Fizz")
    elif(fizz_buzz % 5 == 0):
        print("Buzz")
    elif(fizz_buzz % 3 == 0) and (n % 5 == 0):
        print("FizzBuzz")
    else:
        print(fizz_buzz)
