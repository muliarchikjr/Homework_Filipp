
spisok = []

for _ in range(3):
    pair = tuple(input().split())
    spisok.append(pair)

dictionary = {key : int(value) for key, value in spisok}

product_name = input()
print(int(dictionary[product_name]) * 1.15)

sum_all = 0
for price in dictionary.values():
    sum_all += price
print(sum_all)

