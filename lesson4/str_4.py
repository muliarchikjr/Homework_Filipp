#s = "имя: Дмитрий, фамилия: Иванов, возраст: 18"

elements = input().split(', ')

name = elements[0].split(':')[1]
surname = elements[1].split(':')[1]
age = elements[2].split(':')[1]

print('-', end='')
print(name, surname, age, sep='\n-')