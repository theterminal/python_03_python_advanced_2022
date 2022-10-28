# 20221017 - Python - Python Advanced - Exam Preparation 03 Self
# 02 - Flowers Finder - judge: https://judge.softuni.org/Contests/Practice/Index/3374#0


# _______________ version 1 _________________ judge 100%


matrix = []
size = 8
w = (0, 0)
b = (0, 0)

for row in range(size):
    line = input().split()
    for col in range(size):
        if line[col] == 'w':
            w = (row, col)
        if line[col] == 'b':
            b = (row, col)
    matrix.append(line)

turns = ['w', 'b']

board_matrix = []
board_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

for row in range(8, 0, -1):
    line = []
    for col in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        line.append(f'{col}{row}')
    board_matrix.append(line)

# for row in board_matrix:
#     print(row)

wr, wc = (w[0], w[1])
br, bc = (b[0], b[1])

while True:
    if turns[0] == 'w':
        if w[0] == 0:
            print(f'Game over! White pawn is promoted to a queen at {board_matrix[w[0]][w[1]]}.')
            break

        if (w[0] - 1, w[1] - 1) == b:
            w = (w[0] - 1, w[1] - 1)
            print(f'Game over! White win, capture on {board_matrix[w[0]][w[1]]}.')
            break
        elif (w[0] - 1, w[1] + 1) == b:
            w = (w[0] - 1, w[1] + 1)
            print(f'Game over! White win, capture on {board_matrix[w[0]][w[1]]}.')
            break
        else:
            w = (w[0] - 1, w[1])

        if w[0] == 0:
            print(f'Game over! White pawn is promoted to a queen at {board_matrix[w[0]][w[1]]}.')
            break
    else:
        if b[0] == size - 1:
            print(f'Game over! Black pawn is promoted to a queen at {board_matrix[b[0]][b[1]]}.')
            break

        if (b[0] + 1, b[1] - 1) == w:
            b = (b[0] + 1, b[1] - 1)
            print(f'Game over! Black win, capture on {board_matrix[b[0]][b[1]]}.')
            break
        elif (b[0] + 1, b[1] + 1) == w:
            b = (b[0] + 1, b[1] + 1)
            print(f'Game over! Black win, capture on {board_matrix[b[0]][b[1]]}.')
            break
        else:
            b = (b[0] + 1, b[1])

        if b[0] == size - 1:
            print(f'Game over! Black pawn is promoted to a queen at {board_matrix[b[0]][b[1]]}.')
            break

    turns.reverse()
