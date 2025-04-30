
def to_dict(stroka: str):

    count_symbols = len(stroka)
    count_words = len(stroka.split())
    count_predlozh = len(stroka.split('.'))

    return {'Количество слов' : count_words,
            'Количество символов' : count_symbols,
            'Количество предложений' : count_predlozh-1
            }

def output(dictionary: dict):

    for key, value in dictionary.items():
        print(f'{key} - {value}')


