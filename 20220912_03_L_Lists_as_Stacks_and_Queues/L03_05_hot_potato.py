# 20220912 - Python - Python Advanced - Lists as Stacks and Queues
# 05 - Hot Potato - judge: https://judge.softuni.org/Contests/Practice/Index/1830#4

from collections import deque


# _____________________ version 2 ____________________ judge 100%


names = deque((input().split()))
counter_max = int(input())
counter = 1

while len(names) > 1:
    person = names.popleft()
    if counter == counter_max:
        print(f'Removed {person}')
        counter = 1
    else:
        names.append(person)
    counter += 1
print(f'Last is {names.popleft()}')

# _____________________ version 1 ____________________ judge 100%

names = deque()
names.extend(input().split())
counter_max = int(input())
counter = 1

while len(names) > 0:
    if counter == counter_max:
        if len(names) > 1:
            person = names.popleft()
            print(f'Removed {person}')
            counter = 0
        elif len(names) == 1:
            person = names.popleft()
            print(f'Last is {person}')
    else:
        names.append(names.popleft())
    counter += 1
