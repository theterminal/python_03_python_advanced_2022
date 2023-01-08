# 20221017 - Python - Python Advanced - Exam Preparation 03 Self
# 01 - Stewards - judge: https://judge.softuni.org/Contests/Practice/Index/3534#0


# _______________ version 2 _________________ judge 100%


from collections import deque


seats_in = input().split(', ')
nums_1 = deque(map(int, input().split(', ')))
nums_2 = deque(map(int, input().split(', ')))

taken_seats = []
rotations = 0

while not (rotations == 10 or len(taken_seats) == 3):
    rotations += 1

    nums_1_l = nums_1.popleft()
    nums_2_r = nums_2.pop()
    sum_num = nums_1_l + nums_2_r

    symbol = chr(sum_num)
    current_seat_1 = str(nums_1_l) + symbol
    current_seat_2 = str(nums_2_r) + symbol

    if current_seat_1 not in seats_in and current_seat_2 not in seats_in:
        nums_1.append(nums_1_l)
        nums_2.appendleft(nums_2_r)
        continue

    for seat in [current_seat_1, current_seat_2]:
        if seat in taken_seats:
            break
        if seat in seats_in:
            seats_in.remove(seat)
            taken_seats.append(seat)

print(f'Seat matches: {", ".join(taken_seats)}')
print(f'Rotations count: {rotations}')


# _______________ version 1 _________________ judge 100%


from collections import deque


seats_in = input().split(', ')
nums_1 = deque(map(int, input().split(', ')))
nums_2 = deque(map(int, input().split(', ')))

taken_seats = []
rotations = 0

while not (rotations == 10 or len(taken_seats) == 3):
    sum_num = nums_1[0] + nums_2[-1]
    rotations += 1
    symbol = chr(sum_num)
    current_seat_1 = str(nums_1[0]) + symbol
    current_seat_2 = str(nums_2[-1]) + symbol

    if current_seat_1 in taken_seats or current_seat_2 in taken_seats:
        nums_1.popleft()
        nums_2.pop()
        continue

    if current_seat_1 in seats_in:
        seats_in.remove(current_seat_1)
        taken_seats.append(current_seat_1)
        nums_1.popleft()
        nums_2.pop()
    elif current_seat_2 in seats_in:
        seats_in.remove(current_seat_2)
        taken_seats.append(current_seat_2)
        nums_1.popleft()
        nums_2.pop()
    else:
        nums_1.append(nums_1.popleft())
        nums_2.appendleft(nums_2.pop())

print(f'Seat matches: {", ".join(taken_seats)}')
print(f'Rotations count: {rotations}')
