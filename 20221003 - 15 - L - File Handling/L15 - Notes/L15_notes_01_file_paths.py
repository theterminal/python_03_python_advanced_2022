# 20221003 - Python - Python Advanced - File Handling
# Absolute path, Relative path, Opening a file, Error Handling of non-existing files


from os import path
from os import linesep
# from os import linesep - imports new line separator valid for the used OS!


print('\n--------- Relative and  absolute paths ----------\n')


# from current location, go to a file (L15_01.txt) in the same directory
file_path = './L15 - Problems/L15_01.txt'

# open the file with the specified path
file = open(file_path)

# it returns an object of the specified file
print(file)

# It prints the absolute path converted from the relative given (file_path)
print(path.abspath(file_path))


print('\n-------------------\n')


# from current location (the file we're working in),
# go 2 levels up,
# go into another directory (20220915 - 05 - L - Tuples and Sets),
# open another file (L05_01_count_same_values.py)
file_path = '../../20220915 - 05 - L - Tuples and Sets/L05_01_count_same_values.py'

print(file_path)
print(path.abspath(file_path))                      # it returns the absolute path from the given relative (file_path)


print('\n-------- Error Handling of non existing file -----------\n')


file_path = './not_existing_directory/not_existing_file.txt'

try:
    file = open(file_path)
    print(file)
except FileNotFoundError:
    print(f'{file_path} does not exist!')
finally:
    print('exit')
