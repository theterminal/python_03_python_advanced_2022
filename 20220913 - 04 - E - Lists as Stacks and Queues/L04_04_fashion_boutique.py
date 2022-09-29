# 20220913 - Python - Python Advanced - Lists as Stacks and Queues
# 04 - Fashion Boutique - judge url: https://judge.softuni.org/Contests/Compete/Index/1831#3


# _______________ version 1 _____________ judge 100%


clothes_sequence = list(map(int, input().split()))
capacity_of_one_rack = int(input())

racks_used = 1
current_rack = 0

while len(clothes_sequence) > 0:
    if clothes_sequence[-1] <= (capacity_of_one_rack - current_rack):
        current_rack += clothes_sequence.pop()
    else:
        racks_used += 1
        current_rack = 0
        current_rack += clothes_sequence.pop()

print(racks_used)
