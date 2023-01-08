# 20220923 - Python - Python Advanced - Multidimensional Lists
# 03 - Knight Game - judge url: https://judge.softuni.org/Contests/Compete/Index/3194#2


# _______________ version 2 _________________ judge 100%


board_size = int(input())
matrix = [list(input()) for _ in range(board_size)]
positions = ((-2, 1), (-2, -1), (-1, -2), (-1, 2), (2, 1), (2, -1), (1, 2), (1, -2))
removed_k = 0

while True:
    max_attacks = 0
    k_with_most_attacks_pos = []

    for row in range(board_size):
        for col in range(board_size):
            if matrix[row][col] == 'K':
                attacks = 0

                for pos in positions:
                    pos_row_attack = row + pos[0]
                    pos_col_attack = col + pos[1]

                    if 0 <= pos_row_attack < board_size and 0 <= pos_col_attack < board_size:
                        if matrix[pos_row_attack][pos_col_attack] == 'K':
                            attacks += 1

                if attacks > max_attacks:
                    k_with_most_attacks_pos = [row, col]
                    max_attacks = attacks

    if k_with_most_attacks_pos:
        matrix[k_with_most_attacks_pos[0]][k_with_most_attacks_pos[1]] = '0'
        removed_k += 1
    else:
        break

print(removed_k)


# _______________ version 1 _________________ judge 100%


board_size = int(input())
matrix = [list(input()) for _ in range(board_size)]
win_dict = {}
removed_k = 0

while True:
    max_kill_steps = 0
    k_max_kill_steps_position = []

    for row in range(board_size):
        for col in range(board_size):
            if matrix[row][col] == 'K':
                kill_steps = 0

                if 0 <= row - 2 and col + 1 < board_size and matrix[row - 2][col + 1] == 'K':
                    kill_steps += 1
                if 0 <= row - 1 and col + 2 < board_size and matrix[row - 1][col + 2] == 'K':
                    kill_steps += 1
                if 0 <= row - 2 and 0 <= col - 1 and matrix[row - 2][col - 1] == 'K':
                    kill_steps += 1
                if 0 <= row - 1 and 0 <= col - 2 and matrix[row - 1][col - 2] == 'K':
                    kill_steps += 1
                if row + 2 < board_size and col + 1 < board_size and matrix[row + 2][col + 1] == 'K':
                    kill_steps += 1
                if row + 1 < board_size and col + 2 < board_size and matrix[row + 1][col + 2] == 'K':
                    kill_steps += 1
                if row + 2 < board_size and 0 <= col - 1 and matrix[row + 2][col - 1] == 'K':
                    kill_steps += 1
                if row + 1 < board_size and 0 <= col - 2 and matrix[row + 1][col - 2] == 'K':
                    kill_steps += 1

                if kill_steps > max_kill_steps:
                    max_kill_steps = kill_steps
                    k_max_kill_steps_position = [row, col]

    if k_max_kill_steps_position:
        matrix[k_max_kill_steps_position[0]][k_max_kill_steps_position[1]] = '0'
        removed_k += 1
    else:
        break

print(removed_k)
