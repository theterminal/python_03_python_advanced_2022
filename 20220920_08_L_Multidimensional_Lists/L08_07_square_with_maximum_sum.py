# 20220920 - Python - Python Advanced - Multidimensional Lists
# 07 - Square With Maximum Sum - judge: https://judge.softuni.org/Contests/Practice/Index/1834#6


# _______________ version 1 _________________ judge 100%


rows, columns = list(map(int, input().split(', ')))
matrix = [[int(x) for x in input().split(', ')] for y in range(rows)]

row = col = 0
index = ()
biggest_sum = 0
row_start = col_start = 1_000_000

while True:
    sum_2x2 = 0
    for i in range(2):
        for j in range(2):
            if i == 0 and j == 0:
                index = (row + 1, col + 1)
            sum_2x2 += matrix[row + i][col + j]

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
        break

for row in range(row_start, row_start + 2):
    for col in range(col_start, col_start + 2):
        print(matrix[row][col], end=' ')
    print()

print(biggest_sum)
