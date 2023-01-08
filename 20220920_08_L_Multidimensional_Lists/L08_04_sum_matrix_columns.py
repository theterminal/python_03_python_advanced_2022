# 20220920 - Python - Python Advanced - Multidimensional Lists
# 04 - Sum Matrix Columns - judge url: https://judge.softuni.org/Contests/Practice/Index/1834#3


# _______________ version 1 _________________ judge 100%


rows, columns = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split()] for y in range(rows)]

for col_i in range(columns):
    total = 0
    for row_i in range(len(matrix)):
        total += matrix[row_i][col_i]
    print(total)
