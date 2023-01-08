# 20220927 - Python - Python Advanced - Functions Advanced
# 04 - Numbers Folter - judge: https://judge.softuni.org/Contests/Compete/Index/1839#3


# _______________ version 1 _________________ judge 100%


def even_odd_filter(**kwargs):
    result_dict = {}

    for k, v in kwargs.items():
        if k == 'even':
            result_dict[k] = [x for x in v if x % 2 == 0]
        elif k == 'odd':
            result_dict[k] = [x for x in v if x % 2 == 1]

    return dict(sorted(result_dict.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2]
))
