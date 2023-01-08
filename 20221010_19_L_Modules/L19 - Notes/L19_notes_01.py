# 20221010 - Python - Python Advanced - Modules


# Modules: os, random, termcolor, pyfiglet


# ---------------- from pyfiglet import figlet_format -----------------


from pyfiglet import figlet_format


def print_art(msg):
    ascii_art = figlet_format(msg)
    print(ascii_art)


msg = input("What would you like to print? ")
print_art(msg)


# ---------------- pyfiglet -----------------


# from pyfiglet import figlet_format
# text =figlet_format("Python", font="isometric1")
# print(text)


# ---------------- termcolor -----------------


# from termcolor import colored
# text = colored('Hello World!', 'red', attrs=['underline', 'bold'])
# print(text)
#
# text = colored('Hello, World!', 'red', 'on_grey', ['bold', 'blink'])
# print(text)
#
# text = colored('Hello, World!', 'green')
# print(text)


# ---------------- random --------------------


# import random
# fruits = ["apple", "banana", "cherry"]
#
# random.choice(fruits)
# random.shuffle(fruits)


# ---------------- from os import [function 1], [function 2] ---------------------


# this syntax imports only the listed at the of the import word functions and methods


# from os import linesep, listdir
#
# print(listdir('./'))
# print(f'First string{linesep}Second string')        # 'linesep' is '\n' on this Mac OS X


# ---------------- from os import [function 1] as [choose name] ------------------


# this syntax imports only the listed function as name of your choice


# from os import linesep as my_name_for_this_example, listdir as another_name
#
# print(another_name('./'))
# print(f'First string{my_name_for_this_example}Second string')        # 'linesep' is '\n' on this Mac OS X


# ---------------- from os import * ---------------------


# this syntax imports the whole module (all functions, methods) and NO prefix 'os.' is needed.
# Not a good idea to use it because of the name references of your code and the module.


# from os import *
#
#
# print(listdir('./'))
# print(f'First string{linesep}Second string')        # 'linesep' is '\n' on this Mac OS X


# ---------------- import os ---------------------


# this syntax imports the whole module but prefix 'os.' is needed


# import os
#
# print(os.listdir('./'))
# print(f'First string{os.linesep}Second string')        # 'linesep' is '\n' on this Mac OS X
