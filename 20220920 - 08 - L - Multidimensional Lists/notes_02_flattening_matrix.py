# 20220920 - Python - Python Advanced - Multidimensional Lists


print('\n______ example 1 _________ Flattening a matrix ____________________________\n\n')


matrix_1 = [[1, 2, 3], [4, 5, 6]]
flattened_matrix_1 = [num for sublist in matrix_1 for num in sublist]

print(matrix_1)
print(flattened_matrix_1)
print(sum(flattened_matrix_1))


print('\n______ example 2 _________ Flattening a matrix ____________________________\n')


matrix_2 = [[1, 2, 3], [4, 5, 6]]
flattened_matrix_2 = []

for element in matrix_2:
    flattened_matrix_2.extend(element)

print(matrix_2)
print(flattened_matrix_2)
print(sum(flattened_matrix_2))


print('\n______ example 3 _________ Flattening a matrix ____________________________\n')


matrix_3 = [[1, 2, 3], [4, 5, 6]]
flattened_matrix_3 = []

[flattened_matrix_3.extend(i) for i in matrix_3]

print(matrix_3)
print(flattened_matrix_3)
print(sum(flattened_matrix_3))
