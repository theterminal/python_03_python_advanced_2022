# 20220920 - Python - Python Advanced - Multidimensional Lists


print('\n------- example 1 --------- Creating a matrix -------------------\n')


matrix = []
for _ in range(3):
    matrix.append([])

print(matrix)


print('\n------ example 2 ---------\n')


matrix = []
for _ in range(3):
    row = []
    for i in range(3):
        row.append(i)
    matrix.append([])

print(matrix)


print('\n_______ example 3 ________ Creating a matrix with 0 s _________________\n')


matrix_1 = [0 for i in range(2)]                                                 # [0, 0]
matrix_2 = [[0 for i in range(2)] for j in range(2)]                             # [[0, 0], [0, 0]]
matrix_3 = [[[0 for i in range(2)] for j in range(2)] for k in range(2)]         # [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]

print(matrix_1)
print(matrix_2)
print(matrix_3)


print('\n------ example 4 -------------------\n')


for i in range(len(matrix_3)):
    print(f'---> {matrix_3[i]}')
    for j in range(len(matrix_3[i])):
        print(f'------> {matrix_3[i][j]}')
        for k in range(len(matrix_3[i][j])):
            print(f'---------> {matrix_3[i][j][k]}')


print('\n ______ example 5 _________ Creating a matrix with \'k\'s _________________ \n')


matrix_1 = ['k' for i in range(2)]                                                 # [k, k]
matrix_2 = [['k' for i in range(2)] for j in range(2)]                             # [[k, k], [k, k]]
matrix_3 = [[['k' for i in range(2)] for j in range(2)] for k in range(2)]         # [[[k, k], [k, k]], [[k, k], [k, k]]]

print(matrix_1)
print(matrix_2)
print(matrix_3)


print('\n------ example 6 -------------------\n')


for i in range(len(matrix_3)):
    print(f'---> {matrix_3[i]}')
    for j in range(len(matrix_3[i])):
        print(f'------> {matrix_3[i][j]}')
        for k in range(len(matrix_3[i][j])):
            print(f'---------> {matrix_3[i][j][k]}')


print('\n______ example 7 _________ Creating a matrix with numbers _________________\n')


matrix_4 = [[j for j in range(1, 4)] for i in range(3)]

print(matrix_4)


print('\n______ example 8 _________ Flattening a matrix ____________________________\n')


matrix_5 = [[1, 2, 3], [4, 5, 6]]
flattened_matrix_5 = [num for sublist in matrix_5 for num in sublist]

print(matrix_5)
print(flattened_matrix_5)
print(sum(flattened_matrix_5))
