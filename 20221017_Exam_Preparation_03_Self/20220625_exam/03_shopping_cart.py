# 20221017 - Python - Python Advanced - Exam Preparation 03 Self
# 03 - Shopping Cart - judge: https://judge.softuni.org/Contests/Practice/Index/3515#2


# _______________ version 1 _________________ judge 100%


def shopping_cart(*args):
    meals_dict = {'Pizza': [], 'Soup': [], 'Dessert': []}

    for tuple_ in args:
        if tuple_ == 'Stop':
            break
        meal, product = tuple_[0], tuple_[1]

        if meal == 'Soup' and len(meals_dict[meal]) == 3:
            continue
        elif meal == 'Pizza' and len(meals_dict[meal]) == 4:
            continue
        elif meal == 'Dessert' and len(meals_dict[meal]) == 2:
            continue

        if product not in meals_dict[meal]:
            meals_dict[meal].append(product)

    for value in meals_dict.values():
        if len(value) > 0:
            break
    else:
        return 'No products in the cart!'

    sorted_meals = sorted(meals_dict.items(), key=lambda x: (-len(x[1]), x[0]))
    result = []

    for k, v in sorted_meals:
        result.append(f'{k}:')

        for value in sorted(v):
            result.append(f' - {value}')

    return '\n'.join(result)


print('\n------------------ test 1 ------------------\n')


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))


print('\n------------------ test 2 ------------------\n')


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Dessert', 'milk'),
    ('Pizza', 'ham'),
    'Stop',
))


print('\n------------------ test 3 ------------------\n')


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))


print('\n------------------ test 4 ------------------\n')


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    'Stop',
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
))
