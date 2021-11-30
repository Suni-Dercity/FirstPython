# for the choice of the new oppenent
import random

# the list of the 3 difficulties available
difficulty = (
    {'level': 5},
    {'level': 10},
    {'level': 20},
)

# the list of the 3 characters playable
main_characters = (
    {'name': 'Seong Gi-hun', 'marbles': 15, 'loss': 2, 'gain': 1, 'scream_war': "That was a close one.."},
    {'name': 'Kang Sae-byeok', 'marbles': 25, 'loss': 1, 'gain': 2, 'scream_war': "All will be over soon.."},
    {'name': 'Cho Sang-woo', 'marbles': 35, 'loss': 0, 'gain': 3, 'scream_war': "Everything to survive.."}
)

# the list of the 20 different oppenents available
opponents = (
    {'name': 'Ji-yeong', 'marbles': 15, 'age': 18},
    {'name': 'Oh Il-nam', 'marbles': 10, 'age': 75},
    {'name': 'Han Mi-nyeo', 'marbles': 8, 'age': 19},
    {'name': 'Abdul Ali', 'marbles': 20, 'age': 35},
    {'name': 'Hwang Jun-ho', 'marbles': 2, 'age': 25},
    {'name': 'Jang Deok-su', 'marbles': 8, 'age': 4},
    {'name': 'Kim Yun-tae', 'marbles': 15, 'age': 32},
    {'name': 'Kwak Ja-Hyoung', 'marbles': 20, 'age': 81},
    {'name': 'Beyong-gi', 'marbles': 14, 'age': 30},
    {'name': 'Yoo Sung-joo', 'marbles': 6, 'age': 21},
    {'name': 'Pyeong Mi-Kyong', 'marbles': 4, 'age': 15},
    {'name': 'Ryeom Il', 'marbles': 20, 'age': 22},
    {'name': 'Mi Woong', 'marbles': 17, 'age': 75},
    {'name': 'Han Dong-Min', 'marbles': 13, 'age': 18},
    {'name': 'Gwan Jum', 'marbles': 7, 'age': 99},
    {'name': 'Don Hei-Ran', 'marbles': 20, 'age': 27},
    {'name': 'Moobon Chunghee', 'marbles': 4, 'age': 82},
    {'name': 'Nam Haeun', 'marbles': 19, 'age': 18},
    {'name': 'Eom Ji', 'marbles': 3, 'age': 70},
    {'name': 'Hyeong Mee-Yon', 'marbles': 16, 'age': 18},
)

# To make sure that no value are put at the start of the code
n_opponents = 0
choice_level = ""
choice_character = ""
format_marbles = ""
list_loser = []

# Choice of difficulty for the user
while not choice_level in difficulty:
    choice_level = input("Which difficulty do you want to choose ? Choose wisely\n 1. Easy\n 2. Hard\n 3. Impossible")
    if choice_level == "1":
        choice_level = difficulty[0]
    elif choice_level == "2":
        choice_level = difficulty[1]
    elif choice_level == "3":
        choice_level = difficulty[2]
    else:
        print("If you don't choose correctly, you will get eliminated.\nPlease don't be stupid")

# Choice of character from the series for the user
while not choice_character in main_characters:
    choice_character = input(f'Who are you going to choose ?\n1. Seong Gi-Hun\n2. Kang Sae-byeok\n3. Cho Sang-woo')
    if choice_character == "1":
        choice_character = main_characters[0]
    elif choice_character == "2":
        choice_character = main_characters[1]
    elif choice_character == "3":
        choice_character = main_characters[2]
    else:
        print("If you don't choose correctly, you will get eliminated\nPlease don't be stupid")

# loop for the game
while n_opponents < choice_level['level']:
    if choice_character['marbles'] <= 0:
        print(f"Player {choice_character['name']} is eliminated")
        break
    current_opponent = random.choice(opponents)
    while current_opponent in list_loser:
        current_opponent = random.choice(opponents)
    print(current_opponent['name'])

    if current_opponent['age'] >= 70:
        cheating_answer = False
        if not cheating_answer:
            cheating_time = input("They already have one foot in the grave, want an easy win ?\n 1. Y(es)\n 2. (N)o")
        if cheating_time == "Y":
            cheating_answer = True
            choice_character['marbles'] = choice_character['marbles'] + choice_character['gain']
            print(f'You have won {choice_character["gain"]} marble(s) you monster. Your current number of marbles is {choice_character["marbles"]}')
            print(f"{choice_character['name']} : {choice_character['scream_war']}")
            n_opponents += 1
            list_loser.append(current_opponent)
            if n_opponents == choice_level['level']:
                print(
                    f'Congratulations player {choice_character["name"]}, you have won the game !\n Your reward is the GRAND 'f'total of 45.6 billion of Won')
                break
            continue

    if current_opponent['marbles'] % 2 == 0:
        format_marbles = "even"
    else:
        format_marbles = "odd"

    # print debug
    print(format_marbles)

    answer_player = input('even or odd marbles ?')

    while answer_player != "even" and answer_player != "odd":
        print('It seems that you have not something coherent, please try again')
        answer_player = input('Is it even or odd marbles ?')

    if answer_player == format_marbles:
        choice_character['marbles'] = choice_character['marbles'] + choice_character['gain']
        print(f'You have won {choice_character["gain"]} marble(s), your current number of marbles is {choice_character["marbles"]}')
        print(f"{choice_character['name']} : {choice_character['scream_war']}")
        print(f"{current_opponent['name']} had {current_opponent['marbles']} marbles")
    else:
        choice_character['marbles'] = choice_character['marbles'] - choice_character['loss']
        print(f'You have lost {choice_character["loss"]} marble(s), your current number of marbles is {choice_character["marbles"]}')
        print(f"{current_opponent['name']} had {current_opponent['marbles']} marbles")

    list_loser.append(current_opponent)
    n_opponents += 1

    if n_opponents == choice_level['level']:
        print(f'Congratulations player {choice_character["name"]}, you have won the game !\n Your reward is the GRAND 'f'total of 45.6 billion of Won')
        break