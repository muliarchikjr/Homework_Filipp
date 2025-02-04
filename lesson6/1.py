from datetime import datetime

current_year = datetime.now().year
year = int(input('Введите год рождения : '))
age = 2025 - current_year

if age <= 12:
    print('Ребенок')
elif 13 <= age <= 17:
    print('Подросток')
elif 18 <= age <= 24:
    print('Юноша')
elif 25 <= age <= 55:
    print('В расцвете сил')
elif 56 <= age <= 80:
    print('Пожилой')
else:
    print('Старик')