# 20220916 - Python - Python Advanced - Tuples and Sets
# 04 - Count Symbols - judge url: https://judge.softuni.org/Contests/Compete/Index/1833#3


# _______________ version 1 _________________ judge 100%


string_in = input()
unique = sorted(set(string_in))
string_in_tuple = tuple(string_in)

for el in unique:
    print(f'{el}: {string_in_tuple.count(el)} time/s')
