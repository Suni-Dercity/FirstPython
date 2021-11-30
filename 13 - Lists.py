#  une variable qui peut contenir différents éléments de différents types

ma_liste = ['Sam', True, 27, ['mma', 'box thai', 'moto']]

# afficher Sam
print(ma_liste[0])

# modifier la valeur 27 en 28
ma_liste[2] = 28

# m'afficher le mot mma
print(ma_liste[3][0])

# remplacer 'mma' par 'judo'
ma_liste[3][0] = 'judo'

# afficher une découpe des trois premiers éléments de la liste
print(ma_liste[:3])
print(ma_liste[0:3])

#
# Méthodes
#

# ajouter un élément à la sous liste
ma_liste[3].append('titre')

ma_liste[3].insert(1, 'velo')

# trier par ordre alphabétique croissant les éléments de la sous liste

ma_liste[3].sort()
print(ma_liste)

# copie de ma liste dans une nouvelle variable

new_liste = ma_liste.copy()
print(new_liste)
ma_liste[0] = 'Tom'
print(ma_liste)