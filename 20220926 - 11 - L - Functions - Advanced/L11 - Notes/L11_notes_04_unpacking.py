# 20220926 - Python - Python Advanced - Functions Advanced


print('\n__________ Unpacking list, tuple, set _____________\n')


a, b, *rest = [1, 2, 3, 4, 5]             # list
# a, b, *rest = (1, 2, 3, 4, 5)             # tuple
# a, b, *rest = {1, 2, 3, 4, 5}             # set

print(a)                                    # 1
print(b)                                    # 2
print(*rest)                                # 3 4 5
print(a, b)                                 # 1 2
print(a, b, *rest)                          # 1 2 3 4 5
print(*rest, a, b)                          # 3 4 5 1 2
print(a, *rest, b)                          # 1 3 4 5 2
print(b, *rest, a)                          # 2 3 4 5 1


print('\n------------------\n')


a, *_, b = [1, 2, 3, 4, 5, 6, 7, 8]

print(a, b)                                 # 1 8


print('\n------------------\n')


nums = [10, 20, 30, 40, 50]

print(*nums)
print(*nums, sep=' ')
print(10, 20, 30, 40, 50, sep='<->')


print('\n------------------\n')


def add_two_nums(a, b):
    return a + b


nums = [10, 20]
print(add_two_nums(*nums))


print('\n-------- dictionary unpacking ----------\n')


def info(**kwargs):
    print(kwargs)


info(name='peter', age=123, gender='male')                      # {'name': 'peter', 'age': 123, 'gender': 'male'}


print('\n------ # syntax of unpacking if dictionary has to be passed as **kwarg (first unpack it) ----------\n')


def info(**kwargs):
    print(kwargs)


person = {
    'name': 'peter',
    'age': 23,
    'gender': 'male'
}

info(**person)                                                 # {'name': 'peter', 'age': 123, 'gender': 'male'}


print('\n------- unpacking 2 dictionaries into one ---------\n')


person_1 = {
    'name': 'Peter',
    'age': 234,
    'gender': 'male'
}

person_2 = {
    'country': 'USA',
    'grades': [2, 3, 6]
}

result = {
    **person_1,
    **person_2
}

print(result)


print('\n------- packing 2 dictionaries into one, unpacking it and sending it to the function "persons" ---------\n')


def persons(**kwargs):
    return kwargs


person_1 = {
    'name': 'Peter',
    'age': 234,
    'gender': 'male'
}

person_2 = {
    'name': 'USA',
    'age': 12
}

print(persons(**{**person_1, **person_2}))              # {'name': 'USA', 'age': 12, 'gender': 'male'}
