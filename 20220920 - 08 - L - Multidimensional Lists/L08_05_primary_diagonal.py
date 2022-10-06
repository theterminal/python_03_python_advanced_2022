# 20220920 - Python - Python Advanced - Multidimensional Lists
# 05 - Primary Diagonal - judge url: https://judge.softuni.org/Contests/Practice/Index/1834#4


# _______________ version 1 _________________ judge 100%


size_square_matrix = int(input())

matrix = [[int(x) for x in input().split()] for y in range(size_square_matrix)]

total_primary_diagonal = 0
for i in range(size_square_matrix):
    total_primary_diagonal += matrix[i][i]

print(total_primary_diagonal)
