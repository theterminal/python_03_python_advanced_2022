# 20221017 - Python - Python Advanced - Exam Preparation 03 Self
# 03 - Springtime - judge: https://judge.softuni.org/Contests/Practice/Index/3374#2


# _______________ version 1 _________________ judge 100%


def start_spring(**data):
    output = {}
    result = []

    for k, v in data.items():
        if v not in output.keys():
            output[v] = []
        output[v].append(k)

    output = sorted(output.items(), key=lambda x: (-len(x[1]), x[0]))       # returns tuples of sorted items

    for k, v in output:
        result.append(f'{k}:')

        for value in sorted(v):
            result.append(f'-{value}')

    print(result)

    return '\n'.join(result)


example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower", }
print(start_spring(**example_objects))
