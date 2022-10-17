# 20221003 - Python - Python Advanced - File Handling
# Operations with module 'os'


from os import path, remove, rename


print('\n--------------- path joint with the correct OS separator ---------------\n')


print(path.join('..', 'L15 - Problems', 'L15_01_file_opener.txt'))

# In case you are not sure what is the separator for the current operating system. The answer will return tha path


print('\n--------------- path.split() -------------------------------------------\n')


file_path = '../L15 - Problems/L15_01_file_opener.txt'
print(path.split(file_path))


print('\n--------------- .isdir() -----------------------------------------------\n')


file_path = '../L15 - Problems/L15_01_file_opener.txt'
print(path.isdir(file_path))


print('\n--------------- .exists() -----------------------------------------------\n')


file_path = '../L15 - Problems/L15_01_file_opener.txt'
print(path.exists(file_path))


print('\n--------------- rename() -----------------------------------------------\n')


# dir_path = '.'
#
# old_file_name = 'test_file_02.txt'
# new_file_name = 'test_file_2000.txt'
#
# rename(path.join(dir_path, old_file_name), path.join(dir_path, new_file_name))
# print(f'Renamed {old_file_name} to {new_file_name}')

file_path = 'test_file_02.txt'
rename('./test_file_02.txt', './test_file_2000.txt')

print('\n--------------- rename() -----------------------------------------------\n')


# dir_path = '../'
#
# old_file_name = 'test_file_2000'
# new_file_name = 'test_file_02'
#
# rename(path.join(dir_path, old_file_name), path.join(dir_path, new_file_name))
# print(f'Renamed {old_file_name} to {new_file_name}')
