# 20220926 - Python - Python Advanced - Functions Advanced


print('\n---------- *kwargs ----------\n')  # packing argument into dictionary


def info(**kwargs):
    print('name' in kwargs)
    print(kwargs)


info(first_name='Peter', second_name='Lunn', age=45)

print('\n------------------\n')

info(name='Ivan', age=34, gender='M', country='USA')
