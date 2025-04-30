def is_correct(stroka: str):
    count = 0

    for char in stroka:
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
            if count < 0:
                return False

    return count == 0