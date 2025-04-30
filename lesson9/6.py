# """
# Дан словарь наблюдения за температурой
# {"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}.
# Отсортировать словарь по температуре в порядке возрастания и обратно.
#
# """

temperature = {"day1":18, "day2":22, "day3":7, "day4":11, "day5":1}

sorting = sorted(temperature.items(), key=lambda x : x[1])
print(dict(sorting))