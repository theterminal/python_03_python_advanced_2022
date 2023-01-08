# 20220927 - Python - Python Advanced - Functions Advanced
# 08 - Age Assignment - judge url: https://judge.softuni.org/Contests/Compete/Index/1839#7


# _______________ version 1 _________________ judge 100%


def age_assignment(*args, **kwargs):
    people_dictionary = {}
    result = ''

    for k, v in kwargs.items():
        for name in args:
            if name[0] == k:
                people_dictionary[name] = v
    sorted_people_dictionary = sorted(people_dictionary.items())

    for element in sorted_people_dictionary:
        result += f'{element[0]} is {element[1]} years old.\n'

    return result


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))


# _______________ version 2 _________________ judge 100%


def get_name(names: tuple, letter:str):
    for name in names:
        if name.startswith(letter):
            return name


def age_assignment(*names, **kwargs):
    people = {}
    result = ''

    for k, v in kwargs.items():
        name = get_name(names, k)
        people[name] = v

    sorted_people = dict(sorted(people.items(), key=lambda x: x[0]))

    for name, age in sorted_people.items():
        result += f'{name} is {age} years old.\n'

    return result


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
