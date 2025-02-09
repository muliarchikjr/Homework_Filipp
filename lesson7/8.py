
while True:

    primer = input('Введите пример или "стоп" для завершения: ')
    if primer == 'stop':
        break

    print(eval(primer))
