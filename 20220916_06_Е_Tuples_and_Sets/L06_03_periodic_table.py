# 20220916 - Python - Python Advanced - Tuples and Sets
# 03 - Periodic Table - judge: https://judge.softuni.org/Contests/Compete/Index/1833#2


# _______________ version 1 _________________ judge 100%


lines_in = int(input())
unique_elements = set()

for _ in range(lines_in):
    data = input().split()
    for element in data:
        unique_elements.add(element)

if unique_elements:
    print('\n'.join(unique_elements))
