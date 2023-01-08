from utils_L19_03.print_helper import print_line


def print_triangle(n):
    for row in range(1, n + 1):
        print_line(row)

    for row in range(n - 1, 0, -1):
        print_line(row)


def print_square(n):
    for _ in range(1, n + 1):
        print_line(n)


def print_rectangle(rows, cols):
    for _ in range(1, rows + 1):
        print_line(cols)