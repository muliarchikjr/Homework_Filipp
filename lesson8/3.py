
def factorial(x: int):

    itog = 1
    for i in range(1, x+1):
        itog *= i
    return itog

print(factorial(4))