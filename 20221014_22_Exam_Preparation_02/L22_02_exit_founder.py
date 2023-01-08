# 20221014 - Python - Python Advanced - Exam Preparation 02
# 02 - Exit Founder - judge: https://judge.softuni.org/Contests/Practice/Index/3515#1


# _______________ version 1 _________________ judge 100%


player_1, player_2 = input().split(', ')
matrix = [[x for x in input().split()] for _ in range(6)]

turns = [player_1, player_2]
rest_1 = False
rest_2 = False

while True:
    coordinates_in = input()
    x, y = int(coordinates_in[1]), int(coordinates_in[-2])

    current_player = turns[0]

    if current_player == player_1:
        if rest_1:
            turns.reverse()
            rest_1 = False
            continue
    elif current_player == player_2:
        if rest_2:
            turns.reverse()
            rest_2 = False
            continue

    if matrix[x][y] == 'E':
        print(f'{turns[0]} found the Exit and wins the game!')
        break

    if matrix[x][y] == 'T':
        print(f'{turns[0]} is out of the game! The winner is {turns[1]}.')
        break

    if matrix[x][y] == 'W':
        print(f'{turns[0]} hits a wall and needs to rest.')
        if turns[0] == player_1:
            rest_1 = True
        else:
            rest_2 = True

    turns.reverse()
