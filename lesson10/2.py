
def factorial(n):

    result = 1
    for i in range(1, n):
        result *= i
        yield result

a = factorial(6)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))

