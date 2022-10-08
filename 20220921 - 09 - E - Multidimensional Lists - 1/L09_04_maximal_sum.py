# 20220921 - Python - Python Advanced - Multidimensional Lists
# 04 - Maximal Sum - judge url: https://judge.softuni.org/Contests/Compete/Index/1835#3


# _______________ version 1 _________________ judge 100%


import sys


rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for y in range(rows)]

max_sum = -sys.maxsize
current_elements_in_3x3 = []
matrix_3x3_max_sum = []

for row_i in range(rows - 2):                                                   # loop for the main matrix
    for col_i in range(columns - 2):
        for row_i_3x3 in range(row_i, row_i + 3):                               # loop for the 3x3 matrix
            for col_i_3x3 in range(col_i, col_i + 3):
                current_elements_in_3x3.append(matrix[row_i_3x3][col_i_3x3])

        if sum(current_elements_in_3x3) > max_sum:
            max_sum = sum(current_elements_in_3x3)
            matrix_3x3_max_sum = current_elements_in_3x3.copy()
        current_elements_in_3x3.clear()

print(f'Sum = {max_sum}')


counter = 0
for i in range(9):
    counter += 1
    print(matrix_3x3_max_sum[i], end=' ')
    if counter == 3:
        print()
        counter = 0
