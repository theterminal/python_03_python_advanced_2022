# 20220913 - Python - Python Advanced - Lists as Stacks and Queues
# 07 - Robotics - judge url: https://judge.softuni.org/Contests/Compete/Index/1831#6


# ______________ version 1 _______________ judge 100%


from collections import deque


def convert_hhmmss_to_ss(start_time):                                 # str(hh:mm:ss) -> int(seconds)
    hh, mm, ss = [int(x) for x in start_time.split(':')]
    return (hh * 3600) + (mm * 60) + ss


def convert_seconds_to_hhmmss(ss):                                    # int(seconds) -> str(hh:mm:ss)
    ss %= 86400
    hh = ss // 3600
    ss %= 3600
    mm = ss // 60
    ss %= 60
    return f'{hh:02d}:{mm:02d}:{ss:02d}'


robots_data = input().split(';')
robot_process_time = {}
robot_busy_until = {}

for data in robots_data:
    name, process_time = data.split('-')
    robot_process_time[name] = int(process_time)
    robot_busy_until[name] = -1

start_time_ss = convert_hhmmss_to_ss(input())
products = deque()

while True:
    line_product = input()
    if line_product == 'End':
        break
    products.append(line_product)

while products:
    start_time_ss = (start_time_ss + 1)
    current_product = products.popleft()

    for name, busy_until in robot_busy_until.items():
        if start_time_ss >= busy_until:
            robot_busy_until[name] = start_time_ss + robot_process_time[name]
            print(f'{name} - {current_product} [{convert_seconds_to_hhmmss(start_time_ss)}]')
            break
    else:
        products.append(current_product)
