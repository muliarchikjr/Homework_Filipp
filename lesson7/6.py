
otzyvy = {}

while True:
    username = input()
    if username == 'stop':
        break
    review = input()
    otzyvy[username] = review

print(f'Количество отзывов - {len(otzyvy)}')
print('Пользователи : ', end=' ')
for user in otzyvy.keys():
    print(user, end=', ')

print()
print('Отзывы : ', end=' ')
for user in otzyvy.values():
    print(user, end=', ')
