# 20220919 - Python - Python Advanced - Stacks, Queues, Tuples, Sets
# 02 - Expression Evaluator - judge: https://judge.softuni.org/Contests/Compete/Index/3159#1


# _______________ version 3 _________________ judge 100%


from functools import reduce

data_in_list = input().split()
numbers_list = list()

for i in range(len(data_in_list)):
    if data_in_list[i] not in ['+', '-', '*', '/']:
        numbers_list.append(int(data_in_list[i]))
    else:
        if data_in_list[i] == '+':
            numbers_list = [reduce(lambda x, y: x + y, numbers_list)]

        elif data_in_list[i] == '-':
            numbers_list = [reduce(lambda x, y: x - y, numbers_list)]

        elif data_in_list[i] == '*':
            numbers_list = [reduce(lambda x, y: x * y, numbers_list)]

        elif data_in_list[i] == '/':
            numbers_list = [reduce(lambda x, y: x // y, numbers_list)]

print(*numbers_list)


# _______________ version 2 _________________ judge 100%


from functools import reduce


data_in_list = input().split()
stack = []

for element in data_in_list:
    if element.lstrip('-').isnumeric():
        stack.append(int(element))
    else:
        if element == '+':
            stack = [reduce(lambda x, y: x + y, stack)]  # reduce
        elif element == '-':
            stack = [reduce(lambda x, y: x - y, stack)]
        elif element == '*':
            stack = [reduce(lambda x, y: x * y, stack)]
        elif element == '/':
            stack = [reduce(lambda x, y: x // y, stack)]

print(stack[0])


# _______________ version 1 _________________ judge 100%


import math


data_in_list = input().split()
numbers_list = list()

for i in range(len(data_in_list)):
    if data_in_list[i].isdigit() or (data_in_list[i][0] == '-' and len(data_in_list[i]) > 1):
        numbers_list.append(int(data_in_list[i]))
    else:
        if data_in_list[i] == '+':
            num = sum(numbers_list)
            numbers_list.clear()
            numbers_list.append(num)

        elif data_in_list[i] == '-':
            for j in range(len(numbers_list) - 1):
                numbers_list[0] -= numbers_list[1]
                numbers_list.pop(1)

        elif data_in_list[i] == '*':
            for j in range(len(numbers_list) - 1):
                numbers_list[0] *= numbers_list[1]
                numbers_list.pop(1)

        elif data_in_list[i] == '/':
            for j in range(len(numbers_list) - 1):
                numbers_list[0] = math.floor(numbers_list[0] / numbers_list[1])
                numbers_list.pop(1)

print(*numbers_list)
