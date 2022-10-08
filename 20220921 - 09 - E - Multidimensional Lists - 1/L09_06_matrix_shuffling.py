# 20220921 - Python - Python Advanced - Multidimensional Lists
# 06 - Matrix Shuffling - judge url: https://judge.softuni.org/Contests/Compete/Index/1835#5


# _______________ version 2 _________________ judge 100%


rows, columns = tuple(map(int, input().split()))
matrix = [input().split() for i in range(rows)]

while True:
    command = input()
    if command == 'END':
        break

    command = command.split()
    if 'swap' not in command or len(command) != 5:
        print('Invalid input!')
        continue

    r1, c1, r2, c2 = list(map(int, command[1:]))
    if False in [
        0 <= r1 < rows,
        0 <= c1 < columns,
        0 <= r2 < rows,
        0 <= c2 < columns
    ]:
        print('Invalid input!')
        continue

    p1, p2 = matrix[r1][c1], matrix[r2][c2]
    matrix[r1][c1] = p2
    matrix[r2][c2] = p1

    for row in matrix:
        print(*row)


# _______________ version 1 _________________ judge 100%


rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for i in range(rows)]

while True:
    command = input()
    if command == 'END':
        break

    command = command.split()
    if 'swap' not in command or len(command) != 5:
        print('Invalid input!')
        continue

    command = command[1:]
    r1, c1, r2, c2 = list(map(int, command))

    if False in [
        0 <= r1 < rows,
        0 <= r2 < rows,
        0 <= c1 < columns,
        0 <= c2 < columns,
    ]:
        print('Invalid input!')
        continue

    temp_1 = matrix[r2][c2]
    matrix[r2][c2] = matrix[r1][c1]
    matrix[r1][c1] = temp_1

    for row in matrix:
        print(*row)
