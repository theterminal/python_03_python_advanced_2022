# 20220926 - Python - Python Advanced - Functions Advanced
# 03 - Cheese Showcase - judge url: https://judge.softuni.org/Contests/Practice/Index/1838#2


# _______________ version 1 _________________ judge 100%


def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result_str = ''

    for k, v in sorted_cheeses:
        sorted_values = sorted(v, reverse=True)
        result_str += k + '\n'
        result_str += '\n'.join(str(x) for x in sorted_values) + '\n'

    return result_str


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)


# _______________ version 2 _________________ judge 100%


def sorting_cheeses(**cheeses_dict):
    cheeses_dict = sorted(cheeses_dict.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []

    for (name, quantities) in cheeses_dict:
        result.append(name)
        quantity_list = sorted(quantities, reverse=True)
        result += quantity_list

    return "\n".join([str(x) for x in result])


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
