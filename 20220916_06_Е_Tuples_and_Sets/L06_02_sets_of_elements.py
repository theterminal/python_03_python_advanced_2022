# 20220916 - Python - Python Advanced - Tuples and Sets
# 02 - Sets of Elements - judge url: https://judge.softuni.org/Contests/Compete/Index/1833#1


# _______________ version 1 _________________ judge 100%


n, m = map(int, input().split())

n_set = set()
m_set = set()

for _ in range(n):
    n_set.add(int(input()))

for _ in range(m):
    m_set.add(int(input()))

print('\n'.join(list(map(str, n_set.intersection(m_set)))))
