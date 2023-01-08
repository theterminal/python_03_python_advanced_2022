# 20221022_Python_Advanced_Exam
# 01 - Energy Drinks - judge: https://judge.softuni.org/Contests/Compete/Index/3596#0


from collections import deque


mg_coffeine = deque(map(int, input().split(', ')))
energy_drinks = deque(map(int, input().split(', ')))

total_caffeine = 0

while mg_coffeine and energy_drinks:

    last_caff = mg_coffeine.pop()
    first_en = energy_drinks.popleft()
    current_caffeine = last_caff * first_en

    if total_caffeine + current_caffeine <= 300:
        total_caffeine += current_caffeine
    else:
        energy_drinks.append(first_en)
        total_caffeine -= 30
        if total_caffeine < 0:
            total_caffeine = 0

if energy_drinks:
    print(f'Drinks left: {", ".join(str(n) for n in energy_drinks)}')
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f'Stamat is going to sleep with {total_caffeine} mg caffeine.')
