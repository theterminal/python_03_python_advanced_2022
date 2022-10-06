# 20220920 - Python - Python Advanced - Multidimensional Lists
# 01 - Sum Matrix Elements - judge url: https://judge.softuni.org/Contests/Practice/Index/1834#0


# _______________ version 1 _________________ judge 100%


matrix_r_c = list(map(int, (input().split(', '))))
matrix = []
total = 0

for row in range(matrix_r_c[0]):
    matrix.append([])
    col_elements = list(map(int, input().split(', ')))
    for element in col_elements:
        matrix[row].append(element)
        total += element

print(total)
print(matrix)


# _______________ version 2 _________________ judge 100%


rows, cols = [int(x) for x in input().split(', ')]
matrix = []
total = 0

for row in range(rows):
    col = [int(x) for x in input().split(', ')]
    total += sum(col)
    matrix.append(col)

print(total)
print(matrix)
