# 20220930 - Python - Python Advanced - Error Handling
# 03 - Guess game


import random
from colorama import Fore
# level = int(input(Fore.LIGHTWHITE_EX + 'Select level: '))
# this line will add color from colorama


class InvalidLevelError(Exception):
    pass


try:
    level = int(input(Fore.LIGHTWHITE_EX + 'Select level: '))
except ValueError:
    raise InvalidLevelError('Select level is not valid!')

if level <= 0:
    raise InvalidLevelError('Select level is not valid!')

computer_number = random.randint(1, 10 * level)
play = True

while play:
    try:
        player_number = int(input('Guess the number: '))
    except ValueError:
        print('Enter a number!')
        continue

    if player_number == computer_number:
        print('You guess it!')

        if input('Do you want to play again [ y / n ]') != 'y':
            raise SystemExit
        if input('Do want to stay on the same level [y] or go higher level [up]') != 'up':
            level = level
        else:
            level += 1
        computer_number = random.randint(1, 10 * level)

        print(f'Current level: {level}')
    elif player_number < computer_number:
        print('Higher')
    else:
        print('Lower')
