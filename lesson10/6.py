
def triangular_numbers(n):
    while True:
        for i in range(1, n+1):
            yield int(1 / 2 * i * (i + 1))

tn_gen = triangular_numbers(5)
print(next(tn_gen))
print(next(tn_gen))
print(next(tn_gen))
print(next(tn_gen))