# 20220926 - Python - Python Advanced - Functions Advanced
# 04 - Rectangle - judge: https://judge.softuni.org/Contests/Practice/Index/1838#3


# _______________ version 1 _________________ judge 100%


def rectangle(length, width):
    def area():
        return length * width

    def perimeter():
        return length * 2 + width * 2

    if not isinstance(length, int) or not isinstance(width, int):
        return 'Enter valid values!'

    area_rectangle = area()
    perimeter_rectangle = perimeter()

    return f'Rectangle area: {area_rectangle}\nRectangle perimeter: {perimeter_rectangle}'


print(rectangle(2, 10))
