# 20220916 - Python - Python Advanced - Tuples and Sets
# 05 - The Longest Intersection - judge: https://judge.softuni.org/Contests/Compete/Index/1833#4


# _______________ version 3 _________________ judge 100%


num_N = int(input())
longest_intersection_numbers = []

for i in range(num_N):
    range_1, range_2 = input().split('-')
    range_1_start, range_1_end = map(int, range_1.split(','))
    range_2_start, range_2_end = map(int, range_2.split(','))

    set_1 = set(range(range_1_start, range_1_end + 1))
    set_2 = set(range(range_2_start, range_2_end + 1))

    intersection = set_1.intersection(set_2)

    if len(intersection) > len(longest_intersection_numbers):
        longest_intersection_numbers = list(intersection)

print(f'Longest intersection is {longest_intersection_numbers} with length {len(longest_intersection_numbers)}')


# _______________ version 2 _________________ judge 100%


num_N = int(input())
longest_intersection_numbers = []

for i in range(num_N):
    range_1, range_2 = input().split('-')
    range_1_start, range_1_end = map(int, range_1.split(','))
    range_2_start, range_2_end = map(int, range_2.split(','))

    set_1 = {j for j in range(range_1_start, range_1_end + 1)}
    set_2 = {k for k in range(range_2_start, range_2_end + 1)}

    intersection = set_1.intersection(set_2)

    if len(intersection) > len(longest_intersection_numbers):
        longest_intersection_numbers = list(intersection)

print(f'Longest intersection is {longest_intersection_numbers} with length {len(longest_intersection_numbers)}')


# _______________ version 1 _________________ judge 100%


num_N = int(input())
set_1 = set()
set_2 = set()
longest_intersection_numbers = []

for i in range(num_N):
    range_1, range_2 = input().split('-')
    start_start, start_end = map(int, range_1.split(','))
    end_start, end_end = map(int, range_2.split(','))

    for j in range(start_start, start_end + 1):
        set_1.add(j)

    for k in range(end_start, end_end + 1):
        set_2.add(k)

    intersection = set_1.intersection(set_2)

    if len(intersection) > len(longest_intersection_numbers):
        longest_intersection_numbers = list(intersection)

    set_1.clear()
    set_2.clear()

print(f'Longest intersection is {longest_intersection_numbers} with length {len(longest_intersection_numbers)}')
