
prices = {'a' : 10, 'b' : 20, 'c' : 30, 'd' : 40}
phrase = input()

summa = 0
for c in phrase:
    summa += prices[c]
print(summa)

