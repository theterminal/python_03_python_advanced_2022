# 20220912 - Python - Python Advanced - Lists as Stacks and Queues
# 04 - Water Dispenser - judge url: https://judge.softuni.org/Contests/Practice/Index/1830#3

from collections import deque

# _____________________ version 1 ____________________ judge 100%


water_in_dispenser = int(input())
people = deque()

while True:
    name = input()
    if name == 'Start':
        break

    people.append(name)

while True:
    command = input().split()

    if command[0] == 'End':
        break

    if command[0] != 'refill':
        if water_in_dispenser >= int(command[0]):
            print(f'{people.popleft()} got water')
            water_in_dispenser -= int(command[0])
        else:
            print(f'{people.popleft()} must wait')
    elif command[0] == 'refill':
        water_in_dispenser += int(command[1])

print(f'{water_in_dispenser} liters left')
