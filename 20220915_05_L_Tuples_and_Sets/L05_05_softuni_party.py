# 20220915 - Python - Python Advanced - Tuples and Sets
# 05 - SoftUni Party - judge: https://judge.softuni.org/Contests/Practice/Index/1832#4


# _______________ version 1 _________________ judge 100%


num_guests = int(input())
reservations_set_vip = set()
reservations_set_reg = set()

for i in range(num_guests):
    reservation_in = input()
    if reservation_in[0].isdigit():
        reservations_set_vip.add(reservation_in)
    else:
        reservations_set_reg.add(reservation_in)

while True:
    guest_in = input()
    if guest_in == 'END':
        break

    if guest_in[0].isdigit():
        reservations_set_vip.discard(guest_in)
    else:
        reservations_set_reg.discard(guest_in)

print(len(reservations_set_vip) + len(reservations_set_reg))

if reservations_set_vip:
    print('\n'.join(sorted(list(reservations_set_vip))))
if reservations_set_reg:
    print('\n'.join(sorted(list(reservations_set_reg))))
