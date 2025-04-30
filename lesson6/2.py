login, password, age = input(), input(), int(input())

if (login == 'admin' and password == '123456') or (login == 'vasya' and password == 'vas123' and age < 60) or (login == 'guest' and age >= 18):
    print('доступ разрешен')
else:
    print('доступ запрещен')

