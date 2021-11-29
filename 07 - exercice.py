# convertisseur de poids

# on va demander à l'internaute son poids
# en quelle unité est exprimé ce poids ( (k)ilos or (l)bs )

# si le poids est exprimé en kilos -> convertir en lbs ( weight * 2.2 )
# si le poids est exprimé en lbs -> convertir en kilos (weight * 0.45)

# si l'unité de mesure renseignée n'est ni un kilos ni un lbs alors afficher un msg 'wront unit'

# Bonus : KILOS / kilos / kg / klos
# gérer le cas ou pour l'unité de mesure on a pas un k pour kilos mais KILOS / kilos / kg / klos / kilogrammes

# controller si le poids qu'il nous donne est bien un chiffre
# arrondir le poids converti


# Mega Bonus
# lui reposer la question de l'unité de mesure tant qu'il précise pas un l ou un k
# on va demander à l'internaute son poids

options_kilos = ['kilos', 'kg', 'kilogrammes', 'kgs']

poids = input("How much do you weight ? ")
unite = input("In which units ?").lower()
if poids.isnumeric():
    poids = float(poids)
    if unite in options_kilos : # if unite.startswith('k') :
        poids = poids * 2.2
        print(f'your weight in lbs is {round(poids),2}')
    elif unite.startswith('l'):
        poids = round(poids * 0.45)
        print(f'you weight in kilos is {round(poids),2}')
    else :
        print("Wrong unit")
else:
    print("Please enter a valid number")


