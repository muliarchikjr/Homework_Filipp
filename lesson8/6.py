
def yes_or_no(spisok: list):

    try:

        spisok_int = [int(i) for i in spisok]
        itog = []
        spsiok_int_2 = []

        for i in spisok_int:
            if i in spsiok_int_2:
                itog.append('Yes')
            else:
                itog.append('No')
            spsiok_int_2.append(i)

        return itog

    except TypeError:

        print('Список не целый')
        return False



print(yes_or_no([1,2,3,1,4]))
