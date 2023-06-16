for x in range(1, 21):
   print("x =", x, "X2 =", x*x)

students = ["Александр", "Никита", "Стас", "Гена", "Турбо", "Дюша Метелкин"]
l = len(students)
for i in range(0, l):
    print(students[i])

students = ["Александр", "Никита", "Стас", "Гена", "Турбо", "Дюша Метелкин"]
for i in range(0, len(students)):
    print(students[i])

for student in students:
    print(student)

# Напечатать только нечетные
nums = [1,2,3,4,5,6,7,8,9,10]
for n in nums:
    if(n % 2 == 1):
        print(n)
