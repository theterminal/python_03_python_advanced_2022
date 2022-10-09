# 20220921 - Python - Python Advanced - Multidimensional Lists
# 04 - Maximal Sum - judge url: https://judge.softuni.org/Contests/Compete/Index/1835#3


import sys


rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for y in range(rows)]

max_sum = -sys.maxsize
matrix_n_x_n_size = 3
current_elements_in_nxn = []
matrix_nxn_max_sum = []

for row_i in range(rows - (matrix_n_x_n_size - 1)):                                 # loop for the main matrix
    for col_i in range(columns - (matrix_n_x_n_size - 1)):
        for row_i_nxn in range(row_i, row_i + matrix_n_x_n_size):                   # loop for the 3x3 matrix
            for col_i_nxn in range(col_i, col_i + matrix_n_x_n_size):
                current_elements_in_nxn.append(matrix[row_i_nxn][col_i_nxn])

        if sum(current_elements_in_nxn) > max_sum:
            max_sum = sum(current_elements_in_nxn)
            matrix_nxn_max_sum = current_elements_in_nxn.copy()
        current_elements_in_nxn.clear()

print(f'Sum = {max_sum}')

counter = 0
for i in range(matrix_n_x_n_size * matrix_n_x_n_size):
    counter += 1
    print(matrix_nxn_max_sum[i], end=' ')
    if counter == matrix_n_x_n_size:
        print()
        counter = 0


'''

Program returns the maximum sum of the values of elements of square sub-matrix with size n_x_n within the main matrix.
After that it returns the actual sub-matrix.

* - matrix_n_x_n_size must be <= min size of rows of columns of the main matrix
* - first row of input data is the size of the main matrix '{rows} {columns}'
* - following are row by row all data from the main matrix


---------- Test Data ---------


Input 1:
-----
5 6
1 0 4 3 1 1
1 3 1 3 0 4
6 4 1 2 5 6
2 2 1 5 4 1
3 3 3 6 0 5


Output 2:
------
Sum = 34
2 5 6 
5 4 1 
6 0 5


------------------


Input 2:
-------
20 24
1 0 4 3 1 1 1 0 4 3 1 1 6 4 1 2 5 6 1 0 4 7 1 1
1 3 1 3 0 4 1 0 4 3 1 1 1 0 4 3 1 1 1 0 4 3 1 1
6 4 1 2 5 6 1 0 4 7 1 1 1 0 4 3 1 1 1 0 4 9 7 6
2 2 1 5 4 1 1 0 4 3 3 1 1 0 4 3 1 1 1 0 4 3 1 1
3 3 3 6 0 5 1 0 4 3 1 1 6 4 1 2 5 6 1 0 4 7 1 1
1 0 4 3 1 1 1 0 4 9 7 6 1 3 1 3 0 4 1 0 4 3 1 8
1 3 1 3 0 4 1 0 4 3 1 1 1 0 4 3 1 1 1 0 4 3 1 1
6 4 1 2 5 6 1 0 4 3 9 1 1 0 4 3 1 1 1 0 4 9 7 6
2 2 1 5 4 1 1 0 4 6 1 1 6 4 1 2 5 6 1 0 4 7 1 1
3 3 3 6 0 5 1 0 4 3 5 9 1 3 1 3 0 4 1 0 4 3 1 8
1 0 4 3 1 1 1 0 4 8 1 1 1 0 4 3 1 1 1 0 4 3 1 1
1 3 1 3 0 4 1 0 4 3 1 8 1 3 1 3 0 4 1 0 4 3 1 8
6 4 1 2 5 6 1 0 4 3 1 1 1 0 4 3 1 1 1 0 4 9 7 6
2 2 1 5 9 1 1 0 4 3 1 1 6 4 1 2 5 6 1 0 4 7 1 1
3 3 3 6 0 5 1 0 4 3 1 1 1 3 1 3 0 4 1 0 4 3 1 8
1 0 4 3 1 1 1 0 4 2 1 8 1 0 4 3 1 1 1 0 4 3 1 1
1 3 1 3 0 4 1 0 4 3 1 0 1 3 1 3 0 4 1 0 4 3 1 8
6 4 1 2 5 6 1 0 4 0 1 1 1 0 4 3 1 1 1 0 4 9 7 6
2 2 1 5 4 1 1 0 4 3 1 5 1 3 1 3 0 4 1 0 4 3 1 8
3 3 3 6 0 5 1 0 4 3 1 1 6 4 1 2 5 6 1 0 4 7 1 1


Output 2:
--------
Sum = 44
4 9 7 
4 3 1 
4 3 9 


----------------------------------
'''
