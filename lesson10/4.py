
def fibonacci(n):

    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
        #yield a

m = fibonacci(10)
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))
print(next(m))