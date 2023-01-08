# 20221003 - Python - Python Advanced - File Handling
# File write


print('\n____ .open() ___ .write() ___ .close ___\n')

from os import linesep

file_path = './my_first_file.txt'

file = open(file_path, 'w')
file.write('I just created my first file!' + linesep)       # linesep imports the OS specific new line syntax
file.close()
