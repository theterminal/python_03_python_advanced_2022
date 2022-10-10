# 20220926 - Python - Python Advanced - Functions Advanced


print('\n---------- *args ----------\n')


def say_hello(name):
    print(f'Hi {name}!')


say_hello('Peter')
say_hello(['Peter', 'George'])


print('\n------------------------------\n')


def say_hello_to_many(*args):
    print(f'Hi {args}')
    print(f'Hi second time to, {", ".join(args)}')


say_hello_to_many('Peter', 'George', 'Sam')                         # *args in the function is a tuple!


print('\n------------------------------\n')


say_hello_to_many()


print('\n------------------------------\n')


def one_person_and_many(person, *many):
    print(person)
    print(many)
    print(*many)
    print(person, *many)


one_person_and_many('Jimmy')


print('\n------------------------------\n')


one_person_and_many('George', 'Carl', 'Ilia')


print('\n------------------------------\n')


def some_func(*args):
    print(args)


some_func(1, 2, 3)           # (1, 2, 3)
some_func("peter", "george") # ("peter", "george")
some_func(True, False)       # (True, False)
some_func()
