
def list_sorting_str(list_1: list):

    return list(filter(lambda x : isinstance(x, str), list_1))

def list_sorting_bool(list_1: list):

    return list(filter(lambda x: isinstance(x, bool), list_1))

#print(list_sorting_str([1, 'serr', True, "abc", 4, 5, False]))