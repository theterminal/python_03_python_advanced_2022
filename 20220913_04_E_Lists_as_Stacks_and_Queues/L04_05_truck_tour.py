# 20220913 - Python - Python Advanced - Lists as Stacks and Queues
# 05 - Truck Tour - judge url: https://judge.softuni.org/Contests/Compete/Index/1831#4


# _______________ version 1 _______________ judge 100%


from collections import deque


number_pumps = int(input())
fuel_in_tank = 0
distance_to_go = 0
result_pump = None
flag = 0

fuel_deque = deque()
distance_deque = deque()

for i in range(number_pumps):
    fuel, distance = list(map(int, input().split()))
    fuel_deque.append(fuel)
    distance_deque.append(distance)

if sum(fuel_deque) < sum(distance_deque):
    print('You\'re fucked! The total fuel is less than what is needed for the total distance!')
    exit()

for j in range(number_pumps):
    if flag == 1:
        break

    result_pump = j

    for i in range(number_pumps):
        fuel_in_tank += fuel_deque[i]
        distance_to_go += distance_deque[i]

        if fuel_in_tank < distance_to_go:
            fuel_deque.append(fuel_deque.popleft())
            distance_deque.append(distance_deque.popleft())
            fuel_in_tank = 0
            distance_to_go = 0
            break

        if i == number_pumps - 1:
            flag = 1
            break

print(result_pump)
