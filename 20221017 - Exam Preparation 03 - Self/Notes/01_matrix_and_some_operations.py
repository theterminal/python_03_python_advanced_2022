# Uncomment an example to run it!


print('\n----- ex. 1 -------- reversing a string using stack --------------------\n')


text = list(input(f'Enter a list: '))                    # text = [input()]      - will NOT work
stack = []                                               # stack = list()        - will work

for i in range(len(text)):
    stack.append(text.pop())

print("".join(stack))


# print('\n----- ex. 2 -------- matrix - creating, adding elements to, printing --------------------\n')
#
#
# matrix = []                           # creating an empty list
# print(matrix)
#
# for i in range(10):                   # loop for creating the actual matrix
#     matrix.append([])                 # adding the rows of the matrix
#     for j in range(5):                # loop for adding elements in a row of the matrix
#         matrix[i].append(j)           # adding element in the current row of the matrix
#
# for row in matrix:                    # loop for printing of the matrix
#     print(*row)                       # Unpacking every row without conversion from int to str but cannot remove spaces
#
# for row in matrix:                              # loop for printing of the matrix
#     # print(row)
#     print(''.join([str(n) for n in row]))       # must convert int/float to str in order to join them


# print('\n----- ex. 3 -------------- Entering a matrix and keeping only the odd elements ----------------\n')
#
#
# rows = int(input())                                             # enter num of rows you are entering
# matrix = []
#
# for i in range(rows):
#     row = input().split(",")                                   # enter elements, separated by (,) - 'row' times
#     matrix.append(list(map(int, row)))
#
# evens = [[x for x in row if x % 2 == 0] for row in matrix]
#
# print(evens)


# print('\n----- ex. 4 ----- Entering a matrix and unpacking by rows -------\n')
#
# rows = int(input())
# matrix = [map(int, input().split(', ')) for _ in range(rows)]
#
# for row in matrix:
#     print(*row)


# print('\n----- ex. 5 ----- Information about the types of data in a matrix -----------\n')
#
#
# rows = int(input())                                         # enter num of rows
# matrix = [input().split(', ') for _ in range(rows)]         # enter 'row' times lines for the matrix separating the elements in a line with (, )
#
# for row in matrix:
#     print(*row)
#     print(type(row))
#     print(type(row[0]))


# print('\n----- ex. 6 ------- Traversing a matrix --------------\n')
#
#
# rows, cols = list(map(int, input('Enter row and col in the format: 3, 5\n').split(', ')))
# matrix = [['& ' for n in range(cols)] for _ in range(rows)]
#
#
# print('\n_________ code "A" ____________\n')                          # code "B" = code "A"
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         print(matrix[i][j], end=' ')
#     print()
#
# print('\n_________ code "B" ____________\n')                          # code "B" = code "A"
#
# [print(*num) for num in [j for j in matrix]]


# print('\n----- ex. 7 ---- Sum of all columns in a matrix ---------------\n')
#
#
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# sum_m = 0
#
# for col_i in range(3):
#     for row_i in range(len(matrix)):
#         sum_m += matrix[row_i][col_i]
#
# print(f'\nThe matrix is:\n')
# for row_i in range(len(matrix)):
#     for col_i in range(len(matrix[row_i])):
#         print(matrix[row_i][col_i], end=' ')
#     print()
#
# print(f'\n{sum_m} is the sum of all columns in the given matrix')


# print('\n----- ex. 8 ----- Sum of a specific column from a matrix ---------------\n')
#
#
# matrix = [[1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]]
#
# print(f'\nThe matrix is:\n')
# for row_i in range(len(matrix)):
#     for col_i in range(len(matrix[row_i])):
#         print(matrix[row_i][col_i], end=' ')
#     print()
#
# sum_m = 0
# column = int(input('\nEnter the column number you need the sum of: '))
#
# for col_i in range(len(matrix)):
#     if col_i == column - 1:
#         for row_i in range(len(matrix)):
#             sum_m += matrix[row_i][col_i]
#
# print(f'\n{sum_m} is the sum of the given column')


# print('\n----- ex. 9 ----- sum of a specific row from a matrix ---------------\n')
#
#
# matrix = [[0, 0, 0, 0, 0], [1, 1, 1, 1, 1], [2, 2, 2, 2, 2], [3, 3, 3, 3, 3], [4, 4, 4, 4, 4]]
#
# print(f'\nThe matrix is:\n')
# for row_i in range(len(matrix)):
#     for col_i in range(len(matrix[row_i])):
#         print(matrix[row_i][col_i], end=' ')
#     print()
#
# sum_m = 0
# row = int(input('\nEnter the row number you need the sum of: '))
#
# for row_i in range(len(matrix)):
#     if row_i == row - 1:
#         sum_m = sum(matrix[row_i])
#
# print(f'\n{sum_m} is the sum of the given row')
