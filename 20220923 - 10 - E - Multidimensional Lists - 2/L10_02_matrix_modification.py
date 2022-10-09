# 20220923 - Python - Python Advanced - Multidimensional Lists
# 02 - Matrix Modification - judge url: https://judge.softuni.org/Contests/Compete/Index/3194#1


# _______________ version 1 _________________ judge 100%


size = int(input())
matrix = [[int(x) for x in input().split()] for y in range(size)]

while True:
    command = input().split()
    if command[0] == 'END':
        break
    # action, row, column, value = command[0], int(command[1]), int(command[2]), int(command[3])      # both rows work
    action, row, column, value = [int(x) if x.isdigit() else x for x in input().split()]

    if row < 0 or row >= size or column < 0 or column >= size:
        print('Invalid coordinates')
    elif action == 'Add':
        matrix[row][column] += value
    elif action == 'Subtract':
        matrix[row][column] -= value

for row in matrix:                                                                  # [print(*row) for row in matrix]
    print(*row)
