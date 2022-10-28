# 20221017 - Python - Python Advanced - Exam Preparation 03 Self
# 03 - Naughty or Nice - judge: https://judge.softuni.org/Contests/Practice/Index/3306#2


# _______________ version 1 ________________ judge 100%


def naughty_or_nice_list(kids: list, *args, **kwargs):
    naughty_list = []
    nice_list = []
    not_found_list = []
    result = ""

    for item in args:
        reference_list = [int(x[0]) for x in kids]
        num, behaviour = item.split('-')
        num = int(num)
        if reference_list.count(num) > 1:
            continue

        for tuple_ in kids:
            code, name = tuple_
            if num == tuple_[0]:
                if behaviour == 'Nice':
                    nice_list.append(name)
                    kids.remove(tuple_)
                elif behaviour == 'Naughty':
                    naughty_list.append(name)
                    kids.remove(tuple_)

    for key, value in kwargs.items():
        reference_list_name = [x[1] for x in kids]
        if reference_list_name.count(key) > 1:
            continue

        for tuple_ in kids:
            num, name = tuple_
            if key == name:
                if value == 'Nice':
                    nice_list.append(name)
                    kids.remove(tuple_)
                elif value == 'Naughty':
                    naughty_list.append(name)
                    kids.remove(tuple_)

    for tuple_ in kids:
        not_found_list.append(tuple_[1])

    if nice_list:
        result += f"Nice: {', '.join(nice_list)}" + '\n'
    if naughty_list:
        result += f"Naughty: {', '.join(naughty_list)}" + '\n'
    if not_found_list:
        result += f"Not found: {', '.join(not_found_list)}"

    return result
