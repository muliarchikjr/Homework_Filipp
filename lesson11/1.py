
import functools

def decor(func):
    def wrapper(*args):
        try:
            return func(*args)
        except:
            print(f'Ошибка в функции')

    return wrapper


@decor
def delenie(a: int, b: int):

    return a / b

print(delenie(1, 0))
