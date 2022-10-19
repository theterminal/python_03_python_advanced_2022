# 20221004 - Python - Python Advanced - File Handling


import os


print('\n --- os.listdir() --- List of file names and directories --- \n')


directory = input()

for filename in os.listdir(directory):
    print(filename)


# ----------- Test Data ------------


'''
Input 1:
-------
.             # or any other directory path


Output 1:
--------
List of files and directories in the current directory


-----------------------------------


Input 2:
-------
..            # or any other directory path


Output 2:
--------
List of files and directories one level above the current directory
'''


print('\n ----------- List of file names and directories with their path ------------- \n')


directory = input()

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)
    print(file)


'''
Input 1:
-------
.                     # or any other directory path


Output 1:
--------
List of files and directories in the current directory with their paths


-----------------------------------


Input 2:
-------
..                    # or any other directory path


Output 2:
--------
List of files and directories one level above the current directory with their paths
'''


print('\n ---------- os.walk() ----------  \n')


directory = input()
extensions = {}

for file in os.walk(directory):
    print(file)


'''
Input 1:
-------
.                     # or any other directory path


Output 1:
--------
List of files, directories and subdirectories in the current directory with their paths


-----------------------------------


Input 2:
-------
..                    # or any other directory path like /Users/borasam/PycharmProjects


Output 2:
--------
List of files, directories and subdirectories one level above the current directory with their paths
'''
