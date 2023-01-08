# 20220912 - Python - Python Advanced - Lists as Stacks and Queues
# Supermarket - judge: https://judge.softuni.org/Contests/Practice/Index/1830#2

from collections import deque


# _____________________ version 2 ____________________ judge 100%


q = deque()

while True:
    name = input()
    if name == 'End':
        print(f'{len(q)} people remaining.')
        break

    if name == 'Paid':
        print('\n'.join(q))
        q.clear()
        continue
    q.append(name)


# _____________________ version 1 ____________________ judge 100%


q = deque()

while True:
    name = input()
    if name == 'End':
        print(f'{len(q)} people remaining.')
        break

    if name == 'Paid':
        while len(q) > 0:
            print(q.popleft())
        continue
    q.append(name)
