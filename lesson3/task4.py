n = int(input()) #28573

thousands = n // 1000
hundreds = (n // 100) % 10
tens = (n // 10) % 10
eds = n % 10

print(f'''тысяч - {thousands}
сотни - {hundreds}
десятки - {tens}
единицы - {eds}''')