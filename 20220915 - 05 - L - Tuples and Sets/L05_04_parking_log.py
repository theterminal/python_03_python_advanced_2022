# 20220915 - Python - Python Advanced - Tuples and Sets
# 04 - Parking Lot - judge url: https://judge.softuni.org/Contests/Practice/Index/1832#3


# _______________ version 1 _________________ judge 100%


commands = int(input())
parking_lot = set()

for _ in range(commands):
    car_command = tuple(input().split(', '))
    action, plate = car_command

    if action == 'IN':
        parking_lot.add(plate)
    else:
        parking_lot.remove(plate)

if parking_lot:
    # print('\n'.join(parking_lot))
    for plate in parking_lot:
        print(plate)
else:
    print('Parking Lot is Empty')
