
a1, a2, a3, a4 = input(), input(), input(), input()

if isinstance(a1, float) and isinstance(a2, float) and isinstance(a3, float) and isinstance(a4, float):
    print(True)
elif isinstance(a1, str) or isinstance(a2, str) or isinstance(a3, str) or isinstance(a4, str):
    print(True)
elif (isinstance(a1, int) and isinstance(a3, int)) or (isinstance(a2, int) and isinstance(a4, int)) or (isinstance(a3, int) and isinstance(a4, int)):
    print(True)
else:
    print(False)