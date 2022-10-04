# 20220916 - Python - Python Advanced - Tuples and Sets
# 06 - Battle of Names - judge url: https://judge.softuni.org/Contests/Compete/Index/1833#5


# _______________ version 3 _________________ judge 100%


num_names = int(input())
set_odd = set()
set_even = set()

for i in range(num_names):
    name = input()
    total = 0
    for letter in name:
        total += ord(letter)

    total //= (i + 1)
    if total % 2 == 0:
        set_even.add(total)
    else:
        set_odd.add(total)

sum_odd_set = sum(set_odd)
sum_even_set = sum(set_even)

if sum_odd_set == sum_even_set:
    print(', '.join(map(str, (set_odd.union(set_even)))))
elif sum_odd_set > sum_even_set:
    print(', '.join(map(str, (set_odd.difference(set_even)))))
elif sum_even_set > sum_odd_set:
    print(', '.join(map(str, (set_odd.symmetric_difference(set_even)))))
