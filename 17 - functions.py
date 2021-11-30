# definir une fonction 

def greet_user():
    # systeme de block de python
    print('Hello there, general kenobi !')


# param

def greet_user2(first_name, nationality = 'French'):
    print(f'Hi {first_name}, you are {nationality}')


greet_user2('Antho', 'Allemand')
greet_user2('Suni', 'Espagnole')

list = ['Shoco', 'Suni', 'Antho']

for name in list:
    greet_user2(name)


# return statement

list_numbers = [1872, 11, 239, 192]
list_squared_numbers = []

def square(number):
    return number * number

for number in list_numbers:
    list_squared_numbers.append(square(number))

print(list_squared_numbers)