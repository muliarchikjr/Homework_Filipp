#"Это тестовая <start>строка для изучения<end> строковых операций"

stroka = input()

starting = '<start>'
ending = '<end>'

index_1 = stroka.find(starting) + len(starting)
index_2 = stroka.find(ending)
print(stroka[index_1:index_2])