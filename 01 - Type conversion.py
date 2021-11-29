age = input("How old are u ?")  # la fonction input() nous renvoit toujours du texte

print(type(age))

birth_year = 2021 - int(age)

print(birth_year)
print("You were born in " + str(birth_year))

# Function String
# Literal String interpollation

print(f'You were born in {birth_year}')
