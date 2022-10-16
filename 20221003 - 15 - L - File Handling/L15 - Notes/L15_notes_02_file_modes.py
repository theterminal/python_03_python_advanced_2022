# 20221003 - Python - Python Advanced - File Handling
# File Modes


# The mode argument is optional and specifies the mode for manipulating the file
# Its default value is 'r' - open for reading in text mode
# File modes in Python
# w - open for writing, truncating the file first
# x - create a new file and open it for writing
# a - open for writing, appending to the end of the file if it exists
# t - text mode (default)
# b -  binary mode
# + - open a disk file for updating (reading and writing)

"""
Python file modes from: https://tutorial.eyehunts.com/python/python-file-modes-open-write-append-r-r-w-w-x-etc/
Don’t confuse, read about every mode as below.

r       ->>> for reading – The file pointer is placed at the beginning of the file.
                           This is the default mode.

r+      ->>> Opens a file for both reading and writing
             The file pointer will be at the beginning of the file.

w       ->>> Opens a file for writing only.
             Overwrites the file if the file exists.
             If the file does not exist, creates a new file for writing.

w+      ->>> Opens a file for both writing and reading.
             Overwrites the existing file if the file exists.
             If the file does not exist, it creates a new file for reading and writing.

rb      ->>> Opens a file for reading only in binary format.
             The file pointer is placed at the beginning of the file.

rb+     ->>> Opens a file for both reading and writing in binary format.

wb+     ->>> Opens a file for both writing and reading in binary format.
             Overwrites the existing file if the file exists.
             If the file does not exist, it creates a new file for reading and writing.

a       ->>> Opens a file for appending.
             The file pointer is at the end of the file if the file exists.
             That is, the file is in the append mode.
             If the file does not exist, it creates a new file for writing.

ab      ->>> Opens a file for appending in binary format.
             The file pointer is at the end of the file if the file exists.
             That is, the file is in the append mode.
             If the file does not exist, it creates a new file for writing.

a+      ->>> Opens a file for both appending and reading.
             The file pointer is at the end of the file if the file exists.
             The file opens in the append mode.
             If the file does not exist, it creates a new file for reading and writing.

ab+     ->>> Opens a file for both appending and reading in binary format.
             The file pointer is at the end of the file if the file exists.
             The file opens in the append mode.
             If the file does not exist, it creates a new file for reading and writing.

x       ->>> Open for exclusive creation, failing if the file already exists (Python 3)

"""

file_path = './L15_notes_100.py'

try:
    file = open(file_path, 'x')  # It'll create a new file from 'file_path' if non-existing, else returns an error.
    print(file)
except FileNotFoundError:
    print(f'{file_path} does not exist!')
except FileExistsError:
    print(f'{file_path} already exists!')
finally:
    print('exit')
