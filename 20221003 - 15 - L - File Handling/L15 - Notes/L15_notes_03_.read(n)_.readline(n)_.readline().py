# 20221003 - Python - Python Advanced - File Handling
# File reader


print('\n_______________ .read() _________________\n')


file_path = '../L15_01_file_opener/text.txt'

try:
    file = open(file_path, 'r')
    print(file.read())                         # reads the full content of the file


except FileNotFoundError:
    print('File not found')


print('\n_______________ .read(n) _________________\n')


file_path = '../L15_01_file_opener/text.txt'

try:
    file = open(file_path, 'r')
    print(file.read(10))                         # reads the first 10 bytes form the content of the file

except FileNotFoundError:
    print('File not found')


print('\n________________________________\n')


try:
    file = open(file_path, 'r')
    print(file.read(4))                     # It'll return the first 4 bytes of the file
    print(file.read())                      # the pointer was on byte 2 from the previous operation and continued...

    # if you execute print(file.read()) twice, the second time it'll return empty string.

except FileNotFoundError:
    print('File not found')


print('\n_______________ .readline() ______________________\n')


file_path = '../L15_01_file_opener/text.txt'

try:
    file = open(file_path, 'r')
    print(file.readline())                  # It returns the first line from the file.

except FileNotFoundError:
    print('File not found')


print('\n_______________ .readlines() ______________________\n')


file_path = '../L15_01_file_opener/text.txt'

try:
    file = open(file_path, 'r')
    print(file.readlines())                  # It returns the file in a list format.

except FileNotFoundError:
    print('File not found')


print('\n_______________ .readline() ____ read whole file _____\n')


file_path = '../L15_01_file_opener/text.txt'

try:
    file = open(file_path, 'r')
    while True:
        line = file.readline()
        if not line:
            break
        print(line.strip())
except FileNotFoundError:
    print('File not found')


print('\n_______________ .readline(n) ____ (n) is bytes _____\n')


file_path = '../L15_01_file_opener/text.txt'

try:
    file = open(file_path, 'r')
    while True:
        line = file.readline(10)      # it reads 10 bytes and every iteration of the loop reads 10 more until end of the line and starts the next line until the ene of the file
        if not line:
            break
        print(line.strip())
except FileNotFoundError:
    print('File not found')


print('\n--------- path, open, read, close ------------\n')


file_path = '../L15_01_file_opener/text.txt'
file = open(file_path, 'r')

for line in file:
    print(line)

file.close()


print('\n------------ or --------------\n')


file_path = '../L15_01_file_opener/text.txt'
file = open(file_path, 'r')

for line in file:
    print(line, end='')

file.close()
