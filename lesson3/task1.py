first, sec, third = input(), input(), input()
print(first, sec, third)
print(first, sec, third, sep=' : ')

values = [first, sec, third]
for value in values:
    print(' - ', value)