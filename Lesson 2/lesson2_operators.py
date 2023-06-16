user_login = 'adam'
user_pass = 'Qwerty123456'

login = input("Login: ")
password = input("Password: ")

if (login == user_login) and (password == user_pass):
    print("Secret is open")
else:
    print("Locked")

