
def converter(x: str):

    try:

        x = float(x)

        int_part = f'{x:.2f}'.split('.')[0]
        float_part = f'{x:.2f}'.split('.')[1]

        stroka_itog = ''

        for i, char in enumerate(reversed(int_part)):
            if i > 0 and i % 3 == 0:
                stroka_itog += ' '
            stroka_itog += char

        rubles = stroka_itog[::-1]
        itog = rubles + '.' + float_part + " руб."
        return itog


    except TypeError:

        return 'Что-то не так, невозможно преобразовать в число'

print(converter(1234.45566))
