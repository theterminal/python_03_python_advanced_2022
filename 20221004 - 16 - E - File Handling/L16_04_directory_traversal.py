# 20221004 - Python - Python Advanced - File Handling
# 04 - Directory Traversal

# This file contains 2 versions: Version 1 and Version 2.
# Version 1 is commented out. To run it you must uncomment it and comment out the version 2.


# _______ version 2 _______ Outputs ALL files in the specified directory level and subdirectories) _______________


import os


directory = input()
result = []
extensions = {}

for dir_files in os.walk(directory):
    for filename in dir_files[2]:
        file = os.path.join(directory, filename)

        if '.' in file:
            extension = filename.split('.')[-1]

            if extension not in extensions:
                extensions[extension] = []
            extensions[extension].append(filename)

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    result.append(f'.{extension}\n')

    for file in sorted(files):
        result.append(f'- - - {file}\n')

with open('L16_04_files/report_all_files.txt', 'w') as output:
    output.write(''.join(result))


# _______ version 1 _______ Outputs only files in the specified directory level (not in subdirectories) __________


import os


directory = input()
result = []
extensions = {}

for filename in os.listdir(directory):
    file = os.path.join(directory, filename)

    if os.path.isfile(file):
        extension = filename.split('.')[-1]

        if extension not in extensions:
            extensions[extension] = []
        extensions[extension].append(filename)

extensions = sorted(extensions.items(), key=lambda x: x[0])

for extension, files in extensions:
    result.append(f'.{extension}\n')

    for file in sorted(files):
        result.append(f'- - - {file}\n')

with open('L16_04_files/report.txt', 'w') as output:
    output.write(''.join(result))
