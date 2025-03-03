import functools


def log_decorator(func):
    @functools.wraps(func)
    def wrapper(*args):
        print(f'Выполняется функция {func.__name__} с аргументами {args}')
        result = func(*args)
        return result
    return wrapper

@log_decorator
def hello(name, surname):
    print(f'Привет, {name} {surname}')

hello('Ivan', 'Rakitic')