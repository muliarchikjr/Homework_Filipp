
def square_or_perimetr(a : int, b: int, flag: bool):

    if flag:
        return a*b
    else:
        return (a+b)*2

print(square_or_perimetr(4, 5, True))