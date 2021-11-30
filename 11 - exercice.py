# Bonus
# si l'internaute ne nous donne pas un chiffre entre 1 et 10 alors je lui repose la question sans lui faire
# perdre de point

# Bonus 2
# lui proposer de rejouer la partie à la fin de la première partie
# faire devinner un chiffre secret à l'utilisateur

import random


def jeu(nb_chances, min_num, max_num):
    num_found = False
    answer = input("Do you wanna play ? (Y)es or (N)o").lower()
    if answer == "y":

        # genre un chiffre aléatoire entre 1 et 10
        number = random.randint(min_num, max_num)
        print(number)

        while nb_chances > 0:
            if not num_found:
                question = int(input('Try guessing my number'))
                while question > max_num or question < min_num:
                    print("Choisis un bon chiffre enculé")
                    question = int(input('Try guessing my number'))
                if question == number:
                    num_found = True
                # si le chiffre proposé par l'internaute est supérieur au chiffre secret lui indiquer que son chiffre est
                # trop grand et lui indiquer le nombre de poinds de vie restant
                elif question > number:
                    nb_chances -= 1
                    print('Your number is too high')
                    print(f'Wrong answer, you only have {nb_chances} ')
                # si le chiffre proposé par l'internaute est inférieur au chiffre secret lui indiquer que son chiffre est
                # trop petit et lui indiquer le nombre de poinds de vie restant
                else:
                    nb_chances -= 1
                    print('Your number is too low')
                    print(f'Wrong answer, you only have {nb_chances} ')
            else:
                print('Congratulations, you did it')
                break
        # si il trouve le chiffre secret avant d'avoir écouler ses 3 chances -> la partie s'arrête c'est gagné
        # si il ne trouve pas le chiffre secret avant d'avoir écouler ses 3 chances -> la partie s'arrête c'est perdu
        else:
            print("Sorry, you have lost the game")

        jeu(nb_chances, min_num, max_num)


jeu(3, 1, 10)
