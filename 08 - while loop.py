# Mega bonus

options_kilos = ['k', 'kilos', 'kg', 'kilogrammes', 'kgs']
has_converted = False

while True:
    if not has_converted:
        poids = input("How much do you weight ? ")
        if poids.isnumeric():
            while True:
                unite = input("In which units ?").lower()
                poids = float(poids)
                if unite in options_kilos:  # if unite.startswith('k') :
                    poids = poids * 2.2
                    print(f'your weight in lbs is {round(poids)}')
                    has_converted = True
                elif unite.startswith('l'):
                    poids = round(poids * 0.45)
                    print(f'you weight in kilos is {round(poids)}')
                    has_converted = True
                else:
                    print("Wrong unit")
        else:
            print("Please enter a valid number")
    else:
        print("Bye bye")
        break

