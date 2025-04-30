
def filter_password(spisok: list):

    filtered = list(filter(lambda x : len(x['password']) > 5, spisok))
    return filtered

def is_valid_login(login: str):

    latin_chars = 'qwertzuiopüasdfghjklyxcvbnm'
    digits = '0123456789_'
    flag = True
    for c in login:
        if c not in latin_chars and c not in digits:
            flag = False
            break
    return flag

def filter_login(spisok: list):

    filtered = list(filter(lambda x : is_valid_login(x['login']), spisok))
    return filtered

spisok = [

    {"name":"some_name", "login":"some_login", "password":"some_password" },
    {"name":"rex", "login":"rambo", "password":"deni" },
    {"name":"max", "login":"---", "password":"romeojulietta" }

         ]

print(filter_password(spisok))
print(filter_login(spisok))


