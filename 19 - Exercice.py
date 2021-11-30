# Tombola
import random

# Pour cela vous allez définir 10 participants dans un tuple (femmes, hommes, étrangers)
# Chaque participant sera un dictionnaire avec un prénom, un sexe, et une solde (l'argent sur son compte)
Max = {
    'name': 'Max',
    'sex': 'male',
    'solde': 1000,
    'nationality': 'French'
}
Nathalie = {
    'name': 'Nathalie',
    'sex': 'female',
    'solde': 5000,
    'nationality': 'French'
}
Miriam = {
    'name': 'Miriam',
    'sex': 'female',
    'solde': 4000,
    'nationality': 'Marocaine'
}
Pierre = {
    'name': 'Pierre',
    'sex': 'male',
    'solde': 500,
    'nationality': 'French'
}
Stéphane = {
    'name': 'Stéphane',
    'sex': 'male',
    'solde': 2000,
    'nationality': 'French'
}
Hakim = {
    'name': 'Hakim',
    'sex': 'male',
    'solde': 5000,
    'nationality': 'Turkish'
}
Fatima = {
    'name': 'Fatima',
    'sex': 'female',
    'solde': 300,
    'nationality': 'Congolese'
}
Aziz = {
    'name': 'Aziz',
    'sex': 'male',
    'solde': 10000,
    'nationality': 'Algerian'
}
David = {
    'name': 'David',
    'sex': 'male',
    'solde': 10000,
    'nationality': 'French'
}
Elise = {
    'name': 'Elise',
    'sex': 'female',
    'solde': 4000,
    'nationality': 'French'
}

list_participants = (Max,Nathalie,Miriam,Pierre,Stéphane,Hakim,Fatima,Aziz,David,Elise)
list_winners = []
# Le premier gagnant (du premier tour) gagnera 10k euros
# Le deuxième gagnant (du deuxième tour) gagnera 5k euros
# Le troisième gagnant (du troisième tour) gagnera 1k euros
list_rewards = [10000,5000,1000]
has_female_won = False
print(list_participants)

i = 0

# Il va falloir faire gagner aléatoirement 3 gagnants
while i < 3:
    winner = random.choice(list_participants)

    # si je suis au dernier tour et qu'aucune femme n'a encore gagné et que le dernier gagnant au tour est un homme
    # alors je refais gagner une autre personne jusqu'à avoir une femme française
    if i == 2 and not has_female_won and winner['sex'] == 'male':
        continue

    # Un gagnant ne peut gagner qu'une seule fois
    # Parmis les trois gagnants je dois avoir au moins une femme qui gagne
    if winner not in list_winners: # éviter deux gagnants

        # Mega Bonus (racisteuh mais sexiste)
        # Seul une femme française pourra gagner un prix
        # Un homme étranger pourra gagner
        # si une femme gagne elle doit être french
        if winner['sex'] == 'female' and winner['nationality'] != 'French':
            continue

        if winner['sex'] == 'female':  # si une femme gagne je modifie la valeur du boolean
            has_female_won = True

        # A chaque fois qu'un gagnant gagnera faudra l'annoncer en tant que gagnant
        # Afficher le montant gagné et mettre à jour son soldre et afficher son nouveau solde
        winner['solde'] += list_rewards[i]
        list_winners.append(winner)
        print(f"The winner of tonight is: {winner['name']}, their new solde is {winner['solde']} €")
    i += 1







