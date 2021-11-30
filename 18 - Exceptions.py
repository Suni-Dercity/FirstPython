age = int(input('How old are u ?'))

# si je ne rentre pas un chiffre entier
# je vais avoir une ValueError

# comment faire pour gérer l'erreur et personnalise le msg d'erreur

try:
    age = int(input('How old are you ?'))
except ValueError:
    print('Invalid value')


try:
    number = int(input('Give us a number'))
    result = 1000 / number
    print(result)
except ZeroDivisionError:
    print('Enter a value superior to 0')
except ValueError:
    print('Invalid value')