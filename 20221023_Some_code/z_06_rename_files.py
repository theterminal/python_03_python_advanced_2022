# 20221004 - Python - Python Advanced - File Handling
# Rename All Files in a Specified Directory


# Program for renaming of files in a directory by replacing symbol/s with other symbol/s or no string.


import os
import re


directory = input('Enter directory path: ')
string_to_be_replaced = input('Enter the string contained in the file name, you want to replace: ')
newly_replaced_string = input('Enter a replacing string ("Enter" for no string): ')

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)

    if os.path.isfile(file):
        new_file_name = filename.replace(string_to_be_replaced, newly_replaced_string)
        new_file = '/'.join(re.split(r'[\\/]', file)[:-1]) + '/' + new_file_name

        os.rename(file, new_file)
