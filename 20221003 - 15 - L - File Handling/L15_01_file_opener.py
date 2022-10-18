# 20221003 - Python - Python Advanced - File Handling
# 01 - File Opener


# _______________ version 1 _________________


file_path = 'L15_01_file_opener/text.txt'

try:
    file = open(file_path, 'r')
    print('File found')

except FileNotFoundError:
    print(f'File not found')
