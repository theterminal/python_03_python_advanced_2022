# 20220920 - Python - Python Advanced - Multidimensional Lists
# 03 - Flattened Matrix - judge url: https://judge.softuni.org/Contests/Practice/Index/1834#2


# _______________ version 3 _________________ judge 100%


flattened = [num for sub in [[int(x) for x in input().split(', ')] for y in range(int(input()))] for num in sub]
print(flattened)


# _______________ version 2 _________________ judge 100%

rows = int(input())

flattened = [num for sub in [[int(x) for x in input().split(', ')] for y in range(rows)] for num in sub]

print(flattened)


# _______________ version 1 _________________ judge 100%

rows = int(input())

matrix = [[int(x) for x in input().split(', ')] for y in range(rows)]
flattened = [num for sub in matrix for num in sub]

print(flattened)
