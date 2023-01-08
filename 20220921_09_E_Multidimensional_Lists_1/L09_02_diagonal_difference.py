# 20220921 - Python - Python Advanced - Multidimensional Lists
# 02 - Diagonal Difference - judge: https://judge.softuni.org/Contests/Compete/Index/1835#1


# _______________ version 1 _________________ judge 100%


matrix = [[int(x) for x in input().split()] for y in range(int(input()))]
# matrix = [list(map(int, input().split())) for y in range(int(input()))]                 # done using 'map'

primary_diagonal = []
secondary_diagonal = []

sum_primary_diagonal = 0
sum_secondary_diagonal = 0

last_index = len(matrix) - 1

for i in range(len(matrix)):
    primary_diagonal.append(matrix[i][i])
    secondary_diagonal.append(matrix[i][last_index - i])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
