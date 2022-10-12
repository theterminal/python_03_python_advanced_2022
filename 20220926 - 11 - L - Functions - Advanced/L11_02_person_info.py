# 20220926 - Python - Python Advanced - Functions Advanced
# 02 - Person Info - judge url: https://judge.softuni.org/Contests/Practice/Index/1838#1


# _______________ version 1 _________________ judge 100%


def get_info(name, town, age):
    return f'This is {name} from {town} and he is {age} years old'


person = {
    'name': 'George',
    'town': 'Venice',
    'age': 45
}

print(get_info(**person))
print(get_info(age=45, name='Detelin', town='Washington'))
