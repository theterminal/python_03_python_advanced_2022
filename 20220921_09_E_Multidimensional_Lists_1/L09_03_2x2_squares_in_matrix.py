# 20220921 - Python - Python Advanced - Multidimensional Lists
# 03 - 2x2 Squares in Matrix - judge: https://judge.softuni.org/Contests/Compete/Index/1835#2


# _______________ version 3 _________________ judge 100%


rows, columns = list(map(int, (input().split())))
matrix = [input().split() for y in range(rows)]
counter = 0

for row_i in range(len(matrix)):
    if row_i == rows - 1:
        continue
    for col_i in range(len(matrix[row_i])):
        if col_i == columns - 1:
            continue

        if matrix[row_i][col_i] == matrix[row_i][col_i + 1] == matrix[row_i + 1][col_i] == matrix[row_i + 1][col_i + 1]:
            counter += 1

print(counter)


# _______________ version 2 _________________ judge 100%


rows, columns = list(map(int, (input().split())))
matrix = [[x for x in input().split()] for y in range(rows)]

start_row = start_col = 0
result = 0
current_2x2 = set()

while True:

    for row in range(start_row, start_row + 2):
        for col in range(start_col, start_col + 2):
            current_2x2.add(matrix[row][col])

    if len(current_2x2) == 1:
        result += 1
    current_2x2.clear()

    if start_col < columns - 2:
        start_col += 1
    elif start_col == columns - 2:
        if start_row < rows - 2:
            start_row += 1
            start_col = 0
        elif start_row == rows - 2:
            break

print(result)


# _______________ version 1 _________________ judge 100%


rows, columns = list(map(int, (input().split())))
matrix = [[x for x in input().split()] for y in range(rows)]

start_row = start_col = 0
last_element = 'KUR'
result = 0

while True:
    counter_el_in_2x2 = 0
    counter_identical = 1
    flag = False

    for row in range(start_row, start_row + 2):
        for col in range(start_col, start_col + 2):
            current_element = matrix[row][col]
            if counter_el_in_2x2 == 0:
                last_element = current_element
                counter_el_in_2x2 += 1
                continue

            counter_el_in_2x2 += 1

            if current_element == last_element:
                counter_identical += 1
                if counter_identical == 4:
                    result += 1
                continue
            else:
                flag = True
                break
        if flag:
            break

    if start_col < columns - 2:
        start_col += 1
    elif start_col == columns - 2:
        if start_row < rows - 2:
            start_row += 1
            start_col = 0
        elif start_row == rows - 2:
            break

print(result)
