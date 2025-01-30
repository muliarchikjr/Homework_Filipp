
phrase = input()

spisok_slov = phrase.split()
spisok_unikaln_slov = set(spisok_slov)
print(f'Количество уникальных слов : {len(spisok_unikaln_slov)}')

all_symbols = ''.join(spisok_slov)
all_symbols_list = list(all_symbols)
symbols_unikaln = set(all_symbols_list)
print(f'Количество уникальных символов : {len(symbols_unikaln)}')

#считаем количество вхождений каждого символа
count_symbols = {}
for c in all_symbols_list:
    count_symbols[c] = count_symbols.get(c, 0) + 1

count_symbols_reversed = {value : key for key, value in count_symbols.items()}

#print(count_symbols)
#print(count_symbols_reversed)

print(f'Самый частый символ : {count_symbols_reversed[max(count_symbols_reversed)]}')
