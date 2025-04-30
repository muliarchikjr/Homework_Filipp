
def count_char(stroka: str):

    spisok = list(stroka)
    result = {}

    for c in spisok:
        result[c] = result.get(c, 0) + 1
    return result
