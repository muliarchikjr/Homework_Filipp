
num = int(input())

if num < 20:

    counter = 0
    for i in range(num+1):
        if i % 7 == 0:
            counter +=1
    print(counter)
else:

    counter = 0
    for i in range(num+1):
        if i % 11 == 0:
            counter += 1
    print(counter)