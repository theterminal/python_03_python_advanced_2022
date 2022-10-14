# 20220927 - Python - Python Advanced - Functions Advanced
# 07 - Grocery - judge url: https://judge.softuni.org/Contests/Compete/Index/1839#6


# _______________ version 1 _________________ judge 100%


def grocery_store(**kwargs):
    result = ''

    groceries_sorted = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

    for k, v in groceries_sorted:
        result += f'{k}: {v}\n'

    return result


print(grocery_store(
    bread=5,
    pasta=12,
    eggs=12,
))
