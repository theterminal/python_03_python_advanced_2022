# 20221017 - Python - Python Advanced - Exam Preparation 03 Self
# 04 - Martina Explorer - judge: https://judge.softuni.org/Contests/Practice/Index/3430#1


# _______________ version 3 ______ w/functions ___________ judge 100%


def coordinates_validation(size, x, y):
    x = size - 1 if x < 0 else x
    x = 0 if x > size - 1 else x
    y = size - 1 if y < 0 else y
    y = 0 if y > size - 1 else y

    return x, y


def main_loop(commands, x, y, matrix, size):
    directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}
    deposits = {'Water': 0, 'Metal': 0, 'Concrete': 0}
    deposits_full_names = {'W': 'Water', 'M': 'Metal', 'C': 'Concrete'}

    while commands:
        command = commands.pop(0)
        x += directions[command][0]
        y += directions[command][1]

        x, y = coordinates_validation(size, x, y)

        # current cell tests
        if matrix[x][y] == 'W' or matrix[x][y] == 'M' or matrix[x][y] == 'C':
            print(f'{deposits_full_names[matrix[x][y]]} deposit found at ({x}, {y})')
            deposits[deposits_full_names[matrix[x][y]]] += 1
        elif matrix[x][y] == 'R':
            print(f'Rover got broken at ({x}, {y})')
            break

    return deposits


def locating_rover(size, matrix):
    x, y = 0, 0
    for i in range(size):
        if 'E' in matrix[i]:
            x, y = i, matrix[i].index('E')
    return x, y


def start():
    size = 6
    matrix = [input().split() for n in range(size)]
    commands = input().split(', ')

    x, y = locating_rover(size, matrix)
    deposits = main_loop(commands, x, y, matrix, size)

    if all(deposits.values()):
        print('Area suitable to start the colony.')
    else:
        print('Area not suitable to start the colony.')


start()


# _______________ version 2 _________________ judge 100%


# given information
SIZE = 6
matrix = [input().split() for n in range(SIZE)]
commands = input().split(', ')
x, y = 0, 0

# locating rover's coordinates (can be done in beginning when introducing the matrix)
for i in range(len(matrix)):
    if 'E' in matrix[i]:
        x, y = i, matrix[i].index('E')

# possible direction to move the rover
directions = {'up': (-1, 0), 'down': (1, 0), 'left': (0, -1), 'right': (0, 1)}

# deposits
deposits = {'Water': 0, 'Metal': 0, 'Concrete': 0}
deposits_full_names = {'W': 'Water', 'M': 'Metal', 'C':'Concrete'}

# main loop
while commands:
    command = commands.pop(0)
    x += directions[command][0]
    y += directions[command][1]

    # coordinates validation
    x = SIZE - 1 if x < 0 else x
    x = 0 if x > SIZE - 1 else x
    y = SIZE - 1 if y < 0 else y
    y = 0 if y > SIZE - 1 else y

    # current cell tests
    if matrix[x][y] == 'W' or matrix[x][y] == 'M' or matrix[x][y] == 'C':
        print(f'{deposits_full_names[matrix[x][y]]} deposit found at ({x}, {y})')
        deposits[deposits_full_names[matrix[x][y]]] += 1
    elif matrix[x][y] == 'R':
        print(f'Rover got broken at ({x}, {y})')
        break

# output statement after main loop
if all(deposits.values()):
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')


# -------------------- code variation -------------------


# the following  9 lines can replace lines 39-41 + 'deposits_full_name' dictionary at line 24

# if matrix[x][y] == 'W':
    #     deposits['Water'] += 1
    #     print(f'Water deposit found at ({x}, {y})')
    # elif matrix[x][y] == 'M':
    #     deposits['Metal'] += 1
    #     print(f'Metal deposit found at ({x}, {y})')
    # elif matrix[x][y] == 'C':
    #     deposits['Concrete'] += 1
    #     print(f'Concrete deposit found at ({x}, {y})')


# _______________ version 1 _________________ judge 100%


SIZE = 6

matrix = []
rover_position = []

for row in range(SIZE):
    line = input().split()

    if 'E' in line:
        rover_position = [row, line.index('E')]

    matrix.append(line)

commands = input().split(', ')

deposits = {
    'W': 0,
    'M': 0,
    'C': 0
}
deposits_full_name = {
    'W': 'Water',
    'M': 'Metal',
    'C': 'Concrete'
}
directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}
while commands:
    command = commands.pop(0)

    rover_position[0] += directions[command][0]
    rover_position[1] += directions[command][1]

    for i in range(len(rover_position)):
        if rover_position[i] < 0:
            rover_position[i] = SIZE - 1
        elif rover_position[i] == SIZE:
            rover_position[i] = 0

    position = matrix[rover_position[0]][rover_position[1]]

    if position == 'W' or position == 'M' or position == 'C':
        print(f'{deposits_full_name[position]} deposit found at ({rover_position[0]}, {rover_position[1]})')
        deposits[position] += 1
    elif position == 'R':
        print(f'Rover got broken at ({rover_position[0]}, {rover_position[1]})')
        break

if all(deposits.values()):
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')
