
def summa(a: int, b: int):

    s = a
    while a != b:
        a += 1
        s += a
    return s

print(summa(3, 5))
