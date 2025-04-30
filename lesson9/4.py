
list_original = [1,2,3,4,5,6,7,8,9]
list_copy_1 = list_original.copy()
list_copy_2 = list_original.copy()
list_copy_3 = list_original.copy()

result_1 = list(map(lambda x : x**2, list_copy_1))
result_2 = list(map(lambda x : x+3 if x % 2 == 0 else x, list_copy_2))
result_3 = list(map(lambda x : x*3 if x % 2 != 0 else x*2, list_copy_3))

print(result_1, result_2, result_3, sep='\n')