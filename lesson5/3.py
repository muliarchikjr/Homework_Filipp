d = {'one':11, 'two':22, 'hello':'python', True:False}

element_number = int(input())
spisok = list(d)
element_name = spisok[element_number]

del d[element_name]

print(d)