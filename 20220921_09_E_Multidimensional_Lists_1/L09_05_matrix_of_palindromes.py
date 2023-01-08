# 20220921 - Python - Python Advanced - Multidimensional Lists
# 05 - Matrix of Palindromes - judge: https://judge.softuni.org/Contests/Compete/Index/1835#4


# _______________ version 1 _________________ judge 100%


rows, columns = list(map(int, input().split()))
ascii_a = 97
matrix = []

for row in range(rows):
    sub_matrix = []
    for col in range(columns):
        result = chr(ascii_a + row) + chr(ascii_a + col + row) + chr(ascii_a + row)
        sub_matrix.append(result)

    print(*sub_matrix)
