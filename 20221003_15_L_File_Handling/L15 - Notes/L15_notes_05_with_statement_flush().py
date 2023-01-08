# 20221003 - Python - Python Advanced - File Handling
# 'with' statement, flush() method


print('\n --------- with ---------\n')

# 'with' - safely closes the file at the end of the 'with' block

file_path = 'test_file_01'

with open(file_path, 'w') as file:
    file.write('Created a file. Inserted "Hello!". Closed file and left the building!')


print('\n ---------------- example of opening, reading, printing, closing file -----------\n')


file_path = '../L15_01_file_opener.py'
with open(file_path, 'r') as file:
    for line in file:
        print(file.readline(), end='')


print('\n ---------- flush() -------------')


'''

when writing to a file and executing 'file.flush()' will make the written content to appear immediately!
Else it'll take some time and after ending the writing block the content will appear.
example:

file.write('some text')
file.flush()

'''

