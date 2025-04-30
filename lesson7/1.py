
summa = 0

otsenka = int(input())
counter = 0

while otsenka != 0:
    summa += otsenka
    otsenka = int(input())
    counter += 1

print(summa / counter)
