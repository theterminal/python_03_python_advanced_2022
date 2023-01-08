def args_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)


list_args = [1, 12, 33, 44]
dict_kwargs = {'name': 'Ivan'}

print('\n_________ ex. 1 ___________\n')
args_kwargs(*list_args, **dict_kwargs)

print('\n__________ ex. 2 __________\n')
args_kwargs(*list_args)

print('\n_________ ex. 3 ___________\n')
args_kwargs(**dict_kwargs)
