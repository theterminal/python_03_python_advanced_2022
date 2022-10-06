# 20220920 - Python - Python Advanced - Multidimensional Lists
# 06 - Symbol in Matrix - judge url: https://judge.softuni.org/Contests/Practice/Index/1834#5


# _______________ version 1 _________________ judge 100%


rows = columns = int(input())
matrix = []

for _ in range(rows):
    matrix.append(input())

symbol = input()
flag = False
for row_i in range(rows):
    for col_i in range(columns):
        if matrix[row_i][col_i] == symbol:
            print(f'({row_i}, {col_i})')
            flag = True
            break
    if flag:
        break
else:
    print(f'{symbol} does not occur in the matrix')
