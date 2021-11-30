dict = {
    "0": 'zero',
    "1": 'one',
    "2": 'two',
    "3": 'three',
    "4": 'four',
    "5": 'five',
    "6": 'six',
    "7": 'seven',
    "8": 'eight',
    "9": 'nein'
}
# Donner la possibilité à l'internaute de taper un chiffre (ex 2021)
number = input("Please enter a number")
result = ""

# Il faudra parcourir chaque caractère de la string et le transformer en lettre
for char in number:
    if char.isnumeric():
        # 2 deviendra deux donc 2021 deviendra : deux zéro deux un
        result += dict.get(char) + " "

print(result)





