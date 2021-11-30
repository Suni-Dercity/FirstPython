ma_liste = [2, 2, 5, 8, 4, 5, 9, 9]
unique = []

# Supprimer les valeurs dupliquées de la liste
#unique = list(dict.fromkeys(ma_liste)).copy

for number in ma_liste:
    if number not in ma_liste:
        unique.append(number)

print(unique)