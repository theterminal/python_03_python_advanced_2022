# 20220926 - Python - Python Advanced - Functions Advanced
# Recursion


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(7))
