# 20220913 - Python - Python Advanced - Lists as Stacks and Queues
# 03 - Fast Food - judge url: https://judge.softuni.org/Contests/Compete/Index/1831#2


# _______________ version 1 _______________ judge 100%


from collections import deque

quantity_of_food_for_the_day = int(input())
quantity_of_food_each_order = deque(map(int, (input().split(' '))))

print(max(quantity_of_food_each_order))

while len(quantity_of_food_each_order) > 0:
    if quantity_of_food_each_order[0] > quantity_of_food_for_the_day:
        break
    else:
        quantity_of_food_for_the_day -= quantity_of_food_each_order.popleft()

if len(quantity_of_food_each_order) > 0:
    print(f'Orders left: {" ".join(map(str, quantity_of_food_each_order))}')
else:
    print('Orders complete')
