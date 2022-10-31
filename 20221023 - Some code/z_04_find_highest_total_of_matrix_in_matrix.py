# 20220920 - Python - Python Advanced - Multidimensional Lists
# 07 - Square With Maximum Sum - judge url: https://judge.softuni.org/Contests/Practice/Index/1834#6


# _______________ version 1 _________________ judge 100%


rows = 7
columns = 8

matrix = [
    [10, 11, 12, 13, 14, 15, 16, 17],
    [20, 21, 22, 23, 24, 25, 26, 27],
    [10, 11, 12, 13, 14, 15, 16, 17],
    [20, 21, 22, 23, 24, 25, 26, 27],
    [10, 11, 12, 13, 14, 15, 16, 17],
    [20, 21, 22, 23, 24, 25, 26, 27],
    [30, 31, 32, 33, 34, 35, 36, 37]
]

row = col = 0
counter = 1
index = (0, 0)
biggest_sum = 0

while True:
    sum_2x2 = 0
    for i in range(2):
        for j in range(2):
            if i == 0 and j == 0:
                index = (row + 1, col + 1)
            sum_2x2 += matrix[row + i][col + j]
    print(f'matrix 2x2 # {counter}, sum of elements: {sum_2x2}. It starts from index: {index}')
    counter += 1
    if sum_2x2 > biggest_sum:
        biggest_sum = sum_2x2
        row_start = row
        col_start = col

    if col < columns - 2:
        col += 1
    elif col == columns - 2 and row < rows - 2:
        row += 1
        col = 0
    else:
        print("Out!")
        break

print(f'\n Largest Sum: {biggest_sum} and it strarts from ({row_start}, {col_start})')

for row in range(row_start, row_start + 2):
    for col in range(col_start, col_start + 2):
        print(matrix[row][col], end=' ')
    print()
