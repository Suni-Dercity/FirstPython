course = "Python for beginners"

# en python le typage est dynamique (on peut réaffecter à une variable des valeurs de différents types)
# et le typage est implicite

# le fait de déclarer une variable course et de lui affecter une string
# course devient un objet String contenant des données
# et des actions pré-définies liées à son type
# ces actions on appel ça des méthodes
# une méthode c'est une fonction dans un objet

# on retrouve autant de méthodes que d'objets (méthodes String, number, boolean...)

# trouver la position du mot 'for' dans la String
print(course.find('for'))

# afficher la string en remplacant le 'for' par '4'

print(course.replace('for', '4'))

# savoir si le mot 'for' est dans la string course (méthode ou opérateur)
print('for' in course)

test