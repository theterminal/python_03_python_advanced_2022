# 20221003 - Python - Python Advanced - File Handling
# 03 - File Writer

# _______________ version 2 _________________


from os import linesep


file_path = './L15_03_file_writer/my_first_file.txt'

with open(file_path, 'w') as file:
    file.write('I just created my first file!' + linesep)


# _______________ version 1 _________________


from os import linesep


file_path = './L15_03_file_writer/my_first_file.txt'

file = open(file_path, 'w')
file.write('I just created my first file!' + linesep)
file.close()
