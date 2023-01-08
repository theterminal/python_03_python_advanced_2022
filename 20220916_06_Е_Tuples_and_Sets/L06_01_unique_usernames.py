# 20220916 - Python - Python Advanced - Tuples and Sets
# 01 - Unique Usernames - judge: https://judge.softuni.org/Contests/Compete/Index/1833#0


# _______________ version 1 _________________ judge 100%


number_of_usernames = int(input())
unique_usernames = set()

for _ in range(number_of_usernames):
    unique_usernames.add(input())

if unique_usernames:
    print('\n'.join(unique_usernames))
