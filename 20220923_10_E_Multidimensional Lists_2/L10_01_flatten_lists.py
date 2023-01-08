# 20220923 - Python - Python Advanced - Multidimensional Lists
# 01 - Flatten Lists - judge url: https://judge.softuni.org/Contests/Compete/Index/3194#0


# _______________ version 2 _________________ judge 100%


data_in = input().split('|')
result = []

for string in data_in[::-1]:
    result.extend(string.split())
print(' '.join(result))


# _______________ version 1 _________________ judge 100%


data_in = reversed(input().split('|'))
result = []

for string in data_in:
    elements = string.split()
    for i in range(len(elements)):
        result.append(elements[i])
print(' '.join(result))
