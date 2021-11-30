# les dictionnaires sont des tableaux d'association de clefs/valeurs

Suni = {
    'first_name': 'Sunilaey',
    'name': 'Bitch',
    'age' : 21,
    'is_student': True,
    'hobbies': ['Coding', 'Gaming']
}

# afficher le prénom
print(Suni['first_name'])

# modifier l'age
Suni['age'] = 20
print(Suni)

# afficher la date de naissance de Suni (birth_date)
# si cette clé n'existe pas dans le dictionnaire
# afficher une date par défaut (méthode)
print(Suni.get('birth_date', '24/10/2000'))
print(Suni)