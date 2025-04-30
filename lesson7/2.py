
slova = input().split()
slova_updated = []

for slovo in slova:
    slovo_updated = ''
    for i in range(len(slovo)):
        slovo_updated += slovo[i]*(i+1)
    slova_updated.append(slovo_updated)

print(' '.join(slova_updated))