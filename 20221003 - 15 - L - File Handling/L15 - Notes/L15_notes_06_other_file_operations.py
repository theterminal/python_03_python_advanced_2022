# 20221003 - Python - Python Advanced - File Handling
# Other file operations and methods


import os
# listdir(), rmdir()


print('\n--------- prints list of files and directories on the current level -----------\n')


print(os.listdir('../'))


print('\n------- same as above ----------\n')


directory_list_current_level = os.listdir('../')

for directory in directory_list_current_level:
    print(directory)


print('\n--------- prints list of files and directories one level above -----------\n')


print(os.listdir('../../'))


print('\n------- same as above ----------\n')


directory_list_current_level = os.listdir('../../')

for directory in directory_list_current_level:
    print(directory)


# ------------ rmdir() ---------------- it removes an empty directory
