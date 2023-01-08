# 20220919 - Python - Python Advanced - Stacks, Queues, Tuples, Sets
# 04 - Honey - judge: https://judge.softuni.org/Contests/Compete/Index/3159#3


# _______________ version 1 _________________ judge 100%


from collections import deque


bees_deque = deque(map(int, input().split()))
nectar_list = list(map(int, input().split()))
operators = deque(input().split())
honey_total = 0

while bees_deque and nectar_list:
    if nectar_list[-1] >= bees_deque[0]:
        operator = operators.popleft()
        nectar, bee = nectar_list.pop(), bees_deque.popleft()

        if operator == '+':
            honey_total += abs(bee + nectar)
        elif operator == '-':
            honey_total += abs(bee - nectar)
        elif operator == '*':
            honey_total += abs(bee * nectar)
        else:
            if nectar == 0 or bee == 0:
                continue
            honey_total += abs(bee / nectar)
    else:
        nectar_list.pop()

print(f'Total honey made: {honey_total}')

if bees_deque:
    print(f'Bees left: {", ".join(list(map(str, bees_deque)))}')
if nectar_list:
    print(f'Nectar left: {", ".join(list(map(str, nectar_list)))}')
