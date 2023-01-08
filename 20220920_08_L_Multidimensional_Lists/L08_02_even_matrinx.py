# 20220920 - Python - Python Advanced - Multidimensional Lists
# 02 - Even Matrix - judge: https://judge.softuni.org/Contests/Practice/Index/1834#1


# _______________ version 4 _________________ judge 100%


rows = int(input())
even_matrix = []

[(even_matrix.append([x for x in list(map(int, input().split(', '))) if x % 2 == 0])) for y in range(rows)]

print(even_matrix)


# _______________ version 3 _________________ judge 100%


rows = int(input())
even_matrix = []

for i in range(rows):
    even_matrix.append([x for x in list(map(int, input().split(', '))) if x % 2 == 0])

print(even_matrix)


# _______________ version 2 _________________ judge 100%


rows = int(input())
even_matrix = []

for i in range(rows):
    row = [x for x in list(map(int, input().split(', '))) if x % 2 == 0]
    even_matrix.append(row)

print(even_matrix)


# _______________ version 1 _________________ judge 100%


rows = int(input())

even_matrix = []

for i in range(rows):
    even_matrix.append([])
    row = list(map(int, input().split(', ')))
    for element in row:
        if element % 2 == 0:
            even_matrix[i].append(element)

print(even_matrix)
