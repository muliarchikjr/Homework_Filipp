
def initials(fio: str, flag: bool ):

    dictionary = fio.split()

    if flag:
        return (f'{dictionary[0]} {dictionary[1][0]}.{dictionary[2][0]}.')
    else:
        return (f'{dictionary[1][0]}.{dictionary[2][0]}.{dictionary[0]} ')

print(initials('Сидоров Ян Петрович', False))