# 20220915 - Python - Python Advanced - Tuples and Sets
# 03 - Unique Names - judge: https://judge.softuni.org/Contests/Practice/Index/1832#2


# _______________ version 1 _________________ judge 100%


number_names = int(input())
unique_names = set()

for i in range(number_names):
    unique_names.add(input())

for unique_name in unique_names:
    print(unique_name)


# _______________ version 2 _________________ judge 100%


number_names = int(input())
names = []

for i in range(number_names):
    names.append(input())

unique_names = set(name for name in names)

for name in names:
    print(name)
