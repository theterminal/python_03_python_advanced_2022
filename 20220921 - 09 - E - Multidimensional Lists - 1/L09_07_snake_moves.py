# 20220921 - Python - Python Advanced - Multidimensional Lists
# 07 - Snake Moves - judge url: https://judge.softuni.org/Contests/Compete/Index/1835#6

# _______________ version 2 _________________ judge 100%


rows, columns = tuple(map(int, input().split()))
string = input()
row_list = []
matrix = []
index_str = 0

for row in range(rows):
    for col in range(columns):
        row_list.append(string[index_str % len(string)])            # 'index_str % len(string)' - rotating index
        index_str += 1                                              # 'index += 1'

    result = row_list.copy()

    if len(matrix) % 2 != 0:
        result.reverse()

    matrix.append(result)
    row_list.clear()

for row in matrix:
    print(''.join(row))


# _______________ version 1 _________________ judge 100%


rows, columns = tuple(map(int, input().split()))
string = input()
row_list = []
matrix = []
index_str = 0

for row in range(rows):
    for col in range(columns):
        row_list.append(string[index_str])

        if index_str < len(string) - 1:
            index_str += 1
        else:
            index_str = 0
    result = row_list.copy()

    if len(matrix) % 2 != 0:
        result.reverse()

    matrix.append(result)
    row_list.clear()

for row in matrix:
    print(''.join(row))
