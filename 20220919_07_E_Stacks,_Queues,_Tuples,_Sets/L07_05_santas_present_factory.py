# 20220919 - Python - Python Advanced - Stacks, Queues, Tuples, Sets
# 05 - Santa's Present Factory - judge: https://judge.softuni.org/Contests/Compete/Index/3159#4


# _______________ version 3 _________________ judge 100%


from collections import deque

toys = {
    'Doll': {
        'magic': 150,
        'produced': 0
    },
    'Wooden train': {
        'magic': 250,
        'produced': 0
    },
    'Teddy bear': {
        'magic': 300,
        'produced': 0
    },
    'Bicycle': {
        'magic': 400,
        'produced': 0
    }
}
materials_list = list(map(int, input().split()))                  # int[1: 100]
magic_deque = deque(map(int, input().split()))                    # int[-10: 100]

while materials_list and magic_deque:
    flag = False
    if materials_list[-1] == 0:
        materials_list.pop()
        flag = True
    if magic_deque[0] == 0:
        magic_deque.popleft()
        flag = True
    if flag:
        continue

    product = materials_list[-1] * magic_deque[0]       # present = last materials * first magic

    if product in [150, 250, 300, 400]:

        if product == 150:
            toys['Doll']['produced'] += 1
        elif product == 250:
            toys['Wooden train']['produced'] += 1
        elif product == 300:
            toys['Teddy bear']['produced'] += 1
        elif product == 400:
            toys['Bicycle']['produced'] += 1

        materials_list.pop()
        magic_deque.popleft()
    else:
        if product > 0:
            materials_list[-1] += 15
            magic_deque.popleft()
        elif product < 0:
            materials_list.append(materials_list.pop() + magic_deque.popleft())

if (toys['Doll']['produced'] > 0 and toys['Wooden train']['produced'] > 0) or\
        (toys['Teddy bear']['produced'] > 0 and toys['Bicycle']['produced'] > 0):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials_list:
    print(f'Materials left: {", ".join(map(str, reversed(materials_list)))}')
if magic_deque:
    print(f'Magic left: {", ".join(map(str, magic_deque))}')

for toy in sorted(toys):
    if toys[toy]['produced'] > 0:
        print(f'{toy}: {toys[toy]["produced"]}')


# _______________ version 1 _________________ judge 100%


from collections import deque

materials_deque = deque(map(int, input().split()))              # int[1: 100]
magic_deque = deque(map(int, input().split()))                  # int[-10: 100]
count_doll = count_train = count_bear = count_bicycle = 0

while materials_deque and magic_deque:
    box, magic = materials_deque[-1], magic_deque[0]
    product = box * magic  # present = last box * first magic

    if product == 0:
        if box == 0:
            materials_deque.pop()
        if magic == 0:
            magic_deque.popleft()
        continue

    if product < 0:
        materials_deque.append(materials_deque.pop() + magic_deque.popleft())
        continue

    if product in [150, 250, 300, 400]:
        if product == 150:
            count_doll += 1
        elif product == 250:
            count_train += 1
        elif product == 300:
            count_bear += 1
        else:
            count_bicycle += 1

        materials_deque.pop()
        magic_deque.popleft()
    else:
        materials_deque[-1] += 15
        magic_deque.popleft()

if (count_doll > 0 and count_train > 0) or (count_bear > 0 and count_bicycle > 0):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials_deque:
    print(f'Materials left: {", ".join(map(str, reversed(materials_deque)))}')
if magic_deque:
    print(f'Magic left: {", ".join(map(str, magic_deque))}')

if count_bicycle:
    print(f'Bicycle: {count_bicycle}')
if count_doll:
    print(f'Doll: {count_doll}')
if count_bear:
    print(f'Teddy bear: {count_bear}')
if count_train:
    print(f'Wooden train: {count_train}')
