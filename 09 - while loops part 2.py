# depart
# condition
# incrementation

i = 0 # depart
while i < 5: # condition
    print(f'i : {i}') # le code execute tant que la condition est True
    i += 1 # incrementation
else:
    print('fin de la boucle')

# DRY

list_names = ['Jules', 'Julien', 'Adam', 'Sarah']
print(f'Salut {list_names[0]}')

# depart
i = 1
while i < len(list_names):
    print(f'Salut {list_names[i]}')
    i += 1 # incrementation


#
# Exercice : Afficher en console la forme suivante en utilisant la boucle while
#

#####
##
####
##
##

list_hashtag = [5,2,4,2,2]
i = 0
while i < len(list_hashtag):
    print(list_hashtag[i] * "#")
    i += 1

list_kilos = [100,200,1984,69]
i = 0
while i < len(list_kilos):
    converted_weight = list_kilos[i] * 2.2
    print(f'your weight in lbs is : {round(converted_weight)}')
    i += 1