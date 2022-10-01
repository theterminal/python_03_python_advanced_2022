# 20220915 - Python - Python Advanced - Tuples and Sets
# 01 - Count Same Values - judge url: https://judge.softuni.org/Contests/Practice/Index/1832#0


# _______________ version 1 _________________ judge 100%


numbers_tuple = tuple(map(float, input().split()))
numbers_dict = {}

for el in numbers_tuple:
    if el in numbers_dict.keys():
        numbers_dict[el] += 1
    else:
        numbers_dict[el] = 1

for el, value in numbers_dict.items():
    print(f'{el:.1f} - {value} times')


# _______________ version 2 _________________ judge 100%


numbers_tuple = tuple(map(float, input().split()))

unique_nums = []

for num in numbers_tuple:
    if num not in unique_nums:
        unique_nums.append(num)

for num in unique_nums:
    print(f'{num:.1f} - {numbers_tuple.count(num)} times')
