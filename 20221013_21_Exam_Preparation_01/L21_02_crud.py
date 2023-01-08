# 20221013 - Python - Python Advanced - Exam Preparation 01
# 02 - CRUD - judge: https://judge.softuni.org/Contests/Practice/Index/3534#1


# _______________ version 2 _________________ judge 100%


matrix = [[n for n in input().split()] for _ in range(6)]

start_pos = input().lstrip('(').rstrip(')')
x, y = list(map(int, start_pos.split(', ')))

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    flag = False
    line_in = input()
    if line_in == 'Stop':
        break

    line_in_split = line_in.split(', ')
    command = line_in_split[0]
    direction = line_in_split[1]

    x += directions[direction][0]
    y += directions[direction][1]

    if matrix[x][y] == '.':
        flag = True

    if command == 'Create' and flag:
        symbol = line_in_split[2]
        matrix[x][y] = symbol

    elif command == 'Update' and not flag:
        symbol = line_in_split[2]
        matrix[x][y] = symbol

    elif command == 'Delete' and not flag:
        matrix[x][y] = '.'

    elif command == 'Read' and not flag:
        print(matrix[x][y])

for row in matrix:
    print(*row)


# _______________ version 1 _________________ judge 100%


matrix = [[x for x in input().split()] for _ in range(6)]

start_pos = input().lstrip('(').rstrip(')')
start_x, start_y = start_pos.split(', ')
start_x = int(start_x)
start_y = int(start_y)

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while True:
    line_in = input()
    if line_in == 'Stop':
        break

    line_in_split = line_in.split(', ')
    command = line_in_split[0]
    direction = line_in_split[1]

    if command == 'Create':
        symbol = line_in_split[2]

        start_x += directions[direction][0]
        start_y += directions[direction][1]
        current_x_y = (start_x, start_y)

        if matrix[current_x_y[0]][current_x_y[1]] == '.':
            matrix[current_x_y[0]][current_x_y[1]] = symbol
        else:
            continue

    elif command == 'Update':
        symbol = line_in_split[2]

        start_x += directions[direction][0]
        start_y += directions[direction][1]
        current_x_y = (start_x, start_y)

        if matrix[current_x_y[0]][current_x_y[1]] != '.':
            matrix[current_x_y[0]][current_x_y[1]] = symbol
        else:
            continue

    elif command == 'Delete':
        start_x += directions[direction][0]
        start_y += directions[direction][1]
        current_x_y = (start_x, start_y)

        if matrix[current_x_y[0]][current_x_y[1]] != '.':
            matrix[current_x_y[0]][current_x_y[1]] = '.'
        else:
            continue

    elif command == 'Read':
        start_x += directions[direction][0]
        start_y += directions[direction][1]
        current_x_y = (start_x, start_y)

        if matrix[current_x_y[0]][current_x_y[1]] != '.':
            print(matrix[current_x_y[0]][current_x_y[1]])
        else:
            continue

for row in matrix:
    print(*row)
