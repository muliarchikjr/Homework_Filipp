list_random = [1, 2, 3, 4, 5]

list_random[0], list_random[-1] = list_random[-1], list_random[0]

s = list_random.pop(2)
print(s)
print(list_random)