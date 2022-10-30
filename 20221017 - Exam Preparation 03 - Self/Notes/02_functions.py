# Uncomment a block of code to use the example


def a_function(*data, **dictionary):
    for el in data:
        print(el, end=' ')
    print()

    for k, v in dictionary.items():
        print(k, v)


a_function(1, 2, 3, {'Kiril': 123, 'Ivan': 133})


# def print_nums(a, b, c):
#     print(a, b, c)
#
#
# nums = [1, 2, 3]
#
# print_nums(*nums)


# def print_nums(a, b, c, d):
#     print(a, b, c)
#     print(d)
#
#
# nums = [1, 2, 3, 4]
#
# print_nums(*nums)


# def some_func(name, age):
#     print(f"{name} is {age} years old")
#
#
# person = {'age': 20, 'name': "Peter"}
# some_func(**person)


# def get_info(name, age, town):
#     return f'The name is {name}, the age is {age}, the town is {town}'
#
#
# kwargs = {"name": "John", "town": "Sofia", "age": 20}
# print(get_info(**kwargs))


# def recursive_power(x, y):
#     result = 1
#     if y == 0:
#         return result
#     result = x * recursive_power(x, y - 1)
#     return result
#
#
# print(recursive_power(3, 3))                    # 27
