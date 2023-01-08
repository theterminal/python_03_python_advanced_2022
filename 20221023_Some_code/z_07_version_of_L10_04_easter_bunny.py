# 20220923 - Python - Python Advanced - Multidimensional Lists
# 04 - Easter Bunny - judge: https://judge.softuni.org/Contests/Compete/Index/3194#3

# Different KK version of the problem! It changes the 'B' on all positions (skips the positions with 'X')
# and calculates the max sum of a line from the for possible directions (right, down, left, up).


# _______________ version 2 _________________ 


size_field = int(input())
matrix = [[int(x) if x.isdigit() else x for x in input().split()] for _ in range(size_field)]
bunny_pos, trap_pos = [], []

for r in range(size_field):
    for c in range(size_field):
        total_r, total_d, total_l, total_u = 0, 0, 0, 0
        positions_r, positions_d, positions_l, positions_u = [], [], [], []
        if matrix[r][c] == 'X':
            continue
        bunny_pos = [r, c]
        num = matrix[r][c]
        matrix[r][c] = 'B'

        for row_i in range(size_field):
            for col_i in range(len(matrix[row_i])):

                if matrix[row_i][col_i] == 'B':
                    bunny_pos = [row_i, col_i]
                elif matrix[row_i][col_i] == 'X':
                    trap_pos.append((row_i, col_i))

        for col_i in range(bunny_pos[1], size_field - 1):
            if matrix[bunny_pos[0]][col_i + 1] != 'X':
                total_r += matrix[bunny_pos[0]][col_i + 1]
                positions_r.append([bunny_pos[0], col_i + 1])
            else:
                break

        for row_i in range(bunny_pos[0], size_field - 1):
            if matrix[row_i + 1][bunny_pos[1]] != 'X':
                total_d += matrix[row_i + 1][bunny_pos[1]]
                positions_d.append([row_i + 1, bunny_pos[1]])
            else:
                break

        for col_i in range(bunny_pos[1], 0, -1):
            if matrix[bunny_pos[0]][col_i - 1] != 'X':
                total_l += matrix[bunny_pos[0]][col_i - 1]
                positions_l.append([bunny_pos[0], col_i - 1])
            else:
                break

        for row_i in range(bunny_pos[0], 0, -1):
            if matrix[row_i - 1][bunny_pos[1]] != 'X':
                total_u += matrix[row_i - 1][bunny_pos[1]]
                positions_u.append([row_i - 1, bunny_pos[1]])
            else:
                break

        for row in matrix:
            print(row)
        print()
        matrix[r][c] = num

        direction, position, total = '', '', 0

        if total_r > max(total_d, total_l, total_u):
            direction = 'right'
            position = positions_r
            total = total_r
        elif total_d > max(total_r, total_l, total_u):
            direction = 'down'
            position = positions_d
            total = total_d
        elif total_l > max(total_r, total_d, total_u):
            direction = 'left'
            position = positions_l
            total = total_l
        elif total_u > max(total_r, total_d, total_l):
            direction = 'up'
            position = positions_u
            total = total_u

        print(direction)
        # for row in position:
        #     print(row)
        print(total)
        print('------------------')
        total = 0


'''
____________ Test Data ____________


Input 1:
------------------------------------------------
5
1 3 7 9 11
X 5 4 X 63
7 3 21 95 1
0 1 73 4 9
9 2 33 2 0


Output 1:
-------------------------------------------------
['B', 3, 7, 9, 11]
['X', 5, 4, 'X', 63]
[7, 3, 21, 95, 1]
[0, 1, 73, 4, 9]
[9, 2, 33, 2, 0]

right
30
------------------
[1, 'B', 7, 9, 11]
['X', 5, 4, 'X', 63]
[7, 3, 21, 95, 1]
[0, 1, 73, 4, 9]
[9, 2, 33, 2, 0]

right
27
------------------
[1, 3, 'B', 9, 11]
['X', 5, 4, 'X', 63]
[7, 3, 21, 95, 1]
[0, 1, 73, 4, 9]
[9, 2, 33, 2, 0]

down
131
------------------
[1, 3, 7, 'B', 11]
['X', 5, 4, 'X', 63]
[7, 3, 21, 95, 1]
[0, 1, 73, 4, 9]
[9, 2, 33, 2, 0]


0
------------------
[1, 3, 7, 9, 'B']
['X', 5, 4, 'X', 63]
[7, 3, 21, 95, 1]
[0, 1, 73, 4, 9]
[9, 2, 33, 2, 0]

down
73
------------------
[1, 3, 7, 9, 11]
['X', 'B', 4, 'X', 63]
[7, 3, 21, 95, 1]
[0, 1, 73, 4, 9]
[9, 2, 33, 2, 0]

down
6
------------------
[1, 3, 7, 9, 11]
['X', 5, 'B', 'X', 63]
[7, 3, 21, 95, 1]
[0, 1, 73, 4, 9]
[9, 2, 33, 2, 0]

down
127
------------------
[1, 3, 7, 9, 11]
['X', 5, 4, 'X', 'B']
[7, 3, 21, 95, 1]
[0, 1, 73, 4, 9]
[9, 2, 33, 2, 0]

up
11
------------------
[1, 3, 7, 9, 11]
['X', 5, 4, 'X', 63]
['B', 3, 21, 95, 1]
[0, 1, 73, 4, 9]
[9, 2, 33, 2, 0]

right
120
------------------
[1, 3, 7, 9, 11]
['X', 5, 4, 'X', 63]
[7, 'B', 21, 95, 1]
[0, 1, 73, 4, 9]
[9, 2, 33, 2, 0]

right
117
------------------
[1, 3, 7, 9, 11]
['X', 5, 4, 'X', 63]
[7, 3, 'B', 95, 1]
[0, 1, 73, 4, 9]
[9, 2, 33, 2, 0]

down
106
------------------
[1, 3, 7, 9, 11]
['X', 5, 4, 'X', 63]
[7, 3, 21, 'B', 1]
[0, 1, 73, 4, 9]
[9, 2, 33, 2, 0]

left
31
------------------
[1, 3, 7, 9, 11]
['X', 5, 4, 'X', 63]
[7, 3, 21, 95, 'B']
[0, 1, 73, 4, 9]
[9, 2, 33, 2, 0]

left
126
------------------
[1, 3, 7, 9, 11]
['X', 5, 4, 'X', 63]
[7, 3, 21, 95, 1]
['B', 1, 73, 4, 9]
[9, 2, 33, 2, 0]

right
87
------------------
[1, 3, 7, 9, 11]
['X', 5, 4, 'X', 63]
[7, 3, 21, 95, 1]
[0, 'B', 73, 4, 9]
[9, 2, 33, 2, 0]

right
86
------------------
[1, 3, 7, 9, 11]
['X', 5, 4, 'X', 63]
[7, 3, 21, 95, 1]
[0, 1, 'B', 4, 9]
[9, 2, 33, 2, 0]

down
33
------------------
[1, 3, 7, 9, 11]
['X', 5, 4, 'X', 63]
[7, 3, 21, 95, 1]
[0, 1, 73, 'B', 9]
[9, 2, 33, 2, 0]

up
95
------------------
[1, 3, 7, 9, 11]
['X', 5, 4, 'X', 63]
[7, 3, 21, 95, 1]
[0, 1, 73, 4, 'B']
[9, 2, 33, 2, 0]

left
78
------------------
[1, 3, 7, 9, 11]
['X', 5, 4, 'X', 63]
[7, 3, 21, 95, 1]
[0, 1, 73, 4, 9]
['B', 2, 33, 2, 0]

right
37
------------------
[1, 3, 7, 9, 11]
['X', 5, 4, 'X', 63]
[7, 3, 21, 95, 1]
[0, 1, 73, 4, 9]
[9, 'B', 33, 2, 0]

right
35
------------------
[1, 3, 7, 9, 11]
['X', 5, 4, 'X', 63]
[7, 3, 21, 95, 1]
[0, 1, 73, 4, 9]
[9, 2, 'B', 2, 0]

up
105
------------------
[1, 3, 7, 9, 11]
['X', 5, 4, 'X', 63]
[7, 3, 21, 95, 1]
[0, 1, 73, 4, 9]
[9, 2, 33, 'B', 0]

up
99
------------------
[1, 3, 7, 9, 11]
['X', 5, 4, 'X', 63]
[7, 3, 21, 95, 1]
[0, 1, 73, 4, 9]
[9, 2, 33, 2, 'B']

up
84
------------------
'''
