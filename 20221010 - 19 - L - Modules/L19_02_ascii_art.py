# 20221010 - Python - Python Advanced - Modules
# 02 - ASCII Art


# ----------------- version 1 -------------------


from pyfiglet import figlet_format


text = 'Python 3.10'

print(figlet_format(text))
print(figlet_format(text, font='standard'))
print(figlet_format(text, font='slant'))
print(figlet_format(text, font='big'))
print(figlet_format(text, font='doom'))
print(figlet_format(text, font='graffiti'))
print(figlet_format(text, font='cyberlarge'))
