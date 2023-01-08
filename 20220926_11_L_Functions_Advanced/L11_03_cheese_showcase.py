# 20220926 - Python - Python Advanced - Functions Advanced
# 03 - Cheese Showcase - judge: https://judge.softuni.org/Contests/Practice/Index/1838#2


# _______________ version 1 _________________ judge 100%


def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))       # converts dictionary to a list of sorted tuples
    result_str = ''

    for k, v in sorted_cheeses:
        sorted_values = sorted(v, reverse=True)                                     # 'v' is a list with values
        result_str += k + '\n'                                                      # 'k' is the name of cheese
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
    cheeses_list = sorted(cheeses_dict.items(), key=lambda x: (-len(x[1]), x[0]))   # converts dictionary to a list of sorted tuples

    result = []

    for name, quantities in cheeses_list:
        result.append(name)
        quantity_list = sorted(quantities, reverse=True)            # 'quantities' is a list with values
        result.extend(quantity_list)                                # 'extend()' adds more than one element to a list, 'append()' adds one element to a list
        # result += quantity_list                                   # "result += quantity_list" = "result.extend(quantity_list)"

    return "\n".join([str(x) for x in result])


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)
