# 20221022_Python_Advanced_Exam
# 03 - Hourly Forecast - judge: https://judge.softuni.org/Contests/Compete/Index/3596#2


def forecast(*args):
    weather = {'Sunny': [], 'Cloudy': [], 'Rainy': []}

    for k, v in args:
        weather[v] += [k]

    result = ''
    for condition, locations in weather.items():
        for location in sorted(locations):
            result += f'{location} - {condition}\n'

    return result


print(forecast(
    ("Sofia", "Sunny"),
    ("London", "Cloudy"),
    ("New York", "Sunny")))

print(forecast(
    ("Beijing", "Sunny"),
    ("Hong Kong", "Rainy"),
    ("Tokyo", "Sunny"),
    ("Sofia", "Cloudy"),
    ("Peru", "Sunny"),
    ("Florence", "Cloudy"),
    ("Bourgas", "Sunny")))

print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
