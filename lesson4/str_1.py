fraza = input()
kolvo_slov = len(fraza.split())
kolvo_symvolov = len(fraza)

print(kolvo_symvolov, kolvo_slov)

glasnye = list(filter(lambda x : x in 'уеыаоэяию', fraza ))
print(len(glasnye))
