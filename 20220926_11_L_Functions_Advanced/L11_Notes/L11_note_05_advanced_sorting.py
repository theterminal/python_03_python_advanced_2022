# 20220926 - Python - Python Advanced - Functions Advanced


# 'x' in 'lambda x' is a tuple of the type ('name': age)

# people = {'Ivan': 14, 'Gosho': 19, 'Mimi': 14, 'Ani': 14}
# people = {'Zappa': 54, 'Ziggy': 19, 'Anny': 34, 'Alice': 44, 'Betty': 14}
people = {'Z': 54, 'Za': 19, 'Anny': 34, 'Ali': 34, 'Betty': 14, 'Bet': 34}
print('\n', people, '\n')


# sorts by dictionary key (ascending order)
result = sorted(people.items())
print(result)


# sorts by age (dict. value)(ascending order)
result_2 = sorted(people.items(), key=lambda x: x[1])
print(result_2)


# sorts by age (dict. value) (descending order)
result_3 = sorted(people.items(), key=lambda x: -x[1])
print(result_3)


# sorts by age (ascending), length of name (descending)
result_4 = sorted(people.items(), key=lambda x: (x[1], -len(x[0])))
print(result_4)


# sorts by age (ascending), length of name (ascending)
result_5 = sorted(people.items(), key=lambda x: (x[1], len(x[0])))
print(result_5)


# sorts by age (ascending), length of name (ascending), name (ascending)
result_6 = sorted(people.items(), key=lambda x: (x[1], -len(x[0]), x[0]))
print(result_6)
