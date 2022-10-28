# 20221017 - Python - Python Advanced - Exam Preparation 03 Self
# 01 - Christmas Elves - judge: https://judge.softuni.org/Contests/Practice/Index/3306#0


# _______________ version 1 _________________ judge 100%


energy = list(map(int, input().split()))
materials = list(map(int, input().split()))

total_energy_used = 0
total_toys_made = 0
cycle_counter = 1

while energy and materials:
    if energy[0] < 5:
        energy.pop(0)
        continue

    elif energy[0] < materials[-1]:
        energy.append(energy.pop(0) * 2)

    elif cycle_counter % 3 == 0:
        if energy[0] >= (materials[-1] * 2):
            if cycle_counter % 5 != 0:
                total_toys_made += 2
                total_energy_used += (materials[-1] * 2)
                energy.append(energy.pop(0) - (materials.pop() * 2) + 1)
            else:
                total_energy_used += (materials[-1] * 2)
                energy.append(energy.pop(0) - (materials.pop() * 2))
        else:
            energy.append(energy.pop(0) * 2)

    elif cycle_counter % 5 == 0:
        total_energy_used += materials[-1]
        energy.append(energy.pop(0) - materials.pop())
    else:
        total_toys_made += 1
        total_energy_used += materials[-1]
        energy.append(energy.pop(0) - materials.pop() + 1)

    cycle_counter += 1

print(f'Toys: {total_toys_made}')
print(f'Energy: {total_energy_used}')

if energy:
    print(f'Elves left: {", ".join(str(x) for x in energy)}')

if materials:
    print(f'Boxes left: {", ".join(str(x) for x in materials)}')
