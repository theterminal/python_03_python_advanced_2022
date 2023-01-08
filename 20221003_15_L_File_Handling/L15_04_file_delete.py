# 20221003 - Python - Python Advanced - File Handling
# 04 - File Delete


# _______________ version 1 _________________


from os import remove


try:
    file_path = './my_first_file.txt'
    remove(file_path)
except FileNotFoundError:
    print('File already deleted!')
