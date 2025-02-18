
def counting(c: int):
    while True:
        yield c+1
        c+=1

a = counting(11)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
