# 20221013 - Python - Python Advanced - Exam Preparation 01
# 01 - Collecting Eggs - judge: https://judge.softuni.org/Contests/Practice/Index/3515#0


# _______________ version 2 _________________ judge 100%


egg_list = list(map(int, input().split(', ')))
paper_list = list(map(int, input().split(', ')))
boxes_filled = 0

egg_list.reverse()

while egg_list and paper_list:
    current_egg = egg_list.pop()

    if current_egg <= 0:
        continue

    if current_egg == 13:
        paper_list[0], paper_list[-1] = paper_list[-1], paper_list[0]
        continue

    egg_packed = current_egg + paper_list[-1]

    if egg_packed <= 50:
        boxes_filled += 1
        paper_list.pop()
    else:
        paper_list.pop()


if boxes_filled:
    print(f'Great! You filled {boxes_filled} boxes.')
else:
    print("Sorry! You couldn't fill any boxes!")

if len(egg_list) > 0:
    egg_list.reverse()
    print(f'Eggs left: {", ".join([str(x) for x in egg_list])}')

if len(paper_list) > 0:
    print(f'Pieces of paper left: {", ".join([str(x) for x in paper_list])}')


# _______________ version 1 _________________ judge 100%


from collections import deque


egg_list = deque(map(int, input().split(', ')))
paper_list = deque(map(int, input().split(', ')))
box_size = 50
boxes_filled = 0

while egg_list and paper_list:
    if egg_list[0] <= 0:
        egg_list.popleft()
        continue

    if egg_list[0] == 13:
        egg_list.popleft()
        paper_list[0], paper_list[-1] = paper_list[-1], paper_list[0]
        continue

    egg_packed = egg_list[0] + paper_list[-1]

    if egg_packed <= box_size:
        boxes_filled += 1
        egg_list.popleft()
        paper_list.pop()
    else:
        egg_list.popleft()
        paper_list.pop()


if boxes_filled:
    print(f'Great! You filled {boxes_filled} boxes.')
else:
    print("Sorry! You couldn't fill any boxes!")

if len(egg_list) > 0:
    print(f'Eggs left: {", ".join([str(x) for x in egg_list])}')

if len(paper_list) > 0:
    print(f'Pieces of paper left: {", ".join([str(x) for x in paper_list])}')
