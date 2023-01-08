# 20220926 - Python - Python Advanced - Functions Advanced
# Nested Functions


def func_main():
    def nested_func_1():
        return f'Hello from nested 1'

    def nested_func_2():
        return f'Hello from nested 2'

    def nested_func_3():
        return f'Hello from nested 3'

    result = nested_func_1() + '\n' + nested_func_2() + '\n' + nested_func_3()

    return result


print(func_main())
