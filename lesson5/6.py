
chisla_1 = [int(i) for i in input().split()]
chisla_2 = [int(i) for i in input().split()]
chisla_3 = [int(i) for i in input().split()]

chisla_11 = set(chisla_1)
chisla_22 = set(chisla_2)
chisla_33 = set(chisla_3)


chisla = chisla_1 + chisla_2 + chisla_3

print(*sorted(list((set(chisla)))))
print(*list(set(chisla_1) & set(chisla_2) & set(chisla_3)))
only_in_one = (chisla_11 - chisla_22 - chisla_33) | (chisla_22 - chisla_11 - chisla_33) | (chisla_33 - chisla_11 - chisla_22)
print(*only_in_one)
