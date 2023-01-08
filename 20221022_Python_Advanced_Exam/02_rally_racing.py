# 20221022_Python_Advanced_Exam
# 02 - Rally Racing - judge: https://judge.softuni.org/Contests/Compete/Index/3596#1


size = int(input())
car_num = input()

matrix = []
car_coordinates = [0, 0]
t_indexes = []

for row_i in range(size):
    line = input().split()
    for col_i in range(len(line)):
        if line[col_i] == 'T':
            t_indexes.append([row_i, col_i])
            # line[col_i] = '.'
    matrix.append(line)

total_km = 0

flag_F = False
if matrix[0][0] == 'F':
    flag_F = True

while not flag_F:
    command = input()
    if command == 'End':
        # print(f'Racing car {car_num} DNF.')
        break

    if command == 'left':
        car_coordinates = [car_coordinates[0], car_coordinates[1] - 1]

        if matrix[car_coordinates[0]][car_coordinates[1]] == 'F':
            matrix[car_coordinates[0]][car_coordinates[1]] = '.'
            flag_F = True
            total_km += 10
            break

        if car_coordinates == t_indexes[0]:
            matrix[t_indexes[0][0]][t_indexes[0][1]] = '.'
            matrix[t_indexes[1][0]][t_indexes[1][1]] = '.'
            car_coordinates = t_indexes[1]
            total_km += 30
            continue
        elif car_coordinates == t_indexes[1]:
            matrix[t_indexes[0][0]][t_indexes[0][1]] = '.'
            matrix[t_indexes[1][0]][t_indexes[1][1]] = '.'
            car_coordinates = t_indexes[0]
            total_km += 30
            continue

        if matrix[car_coordinates[0]][car_coordinates[1]] == '.':
            total_km += 10

    elif command == 'right':
        car_coordinates = [car_coordinates[0], car_coordinates[1] + 1]

        if matrix[car_coordinates[0]][car_coordinates[1]] == 'F':
            matrix[car_coordinates[0]][car_coordinates[1]] = '.'
            flag_F = True
            total_km += 10
            break

        if car_coordinates == t_indexes[0]:
            matrix[t_indexes[0][0]][t_indexes[0][1]] = '.'
            matrix[t_indexes[1][0]][t_indexes[1][1]] = '.'
            car_coordinates = t_indexes[1]
            total_km += 30
            continue
        elif car_coordinates == t_indexes[1]:
            matrix[t_indexes[0][0]][t_indexes[0][1]] = '.'
            matrix[t_indexes[1][0]][t_indexes[1][1]] = '.'
            car_coordinates = t_indexes[0]
            total_km += 30
            continue

        if matrix[car_coordinates[0]][car_coordinates[1]] == '.':
            total_km += 10

    elif command == 'up':
        car_coordinates = [car_coordinates[0] - 1, car_coordinates[1]]

        if matrix[car_coordinates[0]][car_coordinates[1]] == 'F':
            matrix[car_coordinates[0]][car_coordinates[1]] = '.'
            flag_F = True
            total_km += 10
            break

        if car_coordinates == t_indexes[0]:
            matrix[t_indexes[0][0]][t_indexes[0][1]] = '.'
            matrix[t_indexes[1][0]][t_indexes[1][1]] = '.'
            car_coordinates = t_indexes[1]
            total_km += 30
            continue
        elif car_coordinates == t_indexes[1]:
            matrix[t_indexes[0][0]][t_indexes[0][1]] = '.'
            matrix[t_indexes[1][0]][t_indexes[1][1]] = '.'
            car_coordinates = t_indexes[0]
            total_km += 30
            continue

        if matrix[car_coordinates[0]][car_coordinates[1]] == '.':
            total_km += 10

    elif command == 'down':
        car_coordinates = [car_coordinates[0] + 1, car_coordinates[1]]

        if matrix[car_coordinates[0]][car_coordinates[1]] == 'F':
            matrix[car_coordinates[0]][car_coordinates[1]] = '.'
            flag_F = True
            total_km += 10
            break

        if car_coordinates == t_indexes[0]:
            matrix[t_indexes[0][0]][t_indexes[0][1]] = '.'
            matrix[t_indexes[1][0]][t_indexes[1][1]] = '.'
            car_coordinates = t_indexes[1]
            total_km += 30
            continue
        elif car_coordinates == t_indexes[1]:
            matrix[t_indexes[0][0]][t_indexes[0][1]] = '.'
            matrix[t_indexes[1][0]][t_indexes[1][1]] = '.'
            car_coordinates = t_indexes[0]
            total_km += 30
            continue

        if matrix[car_coordinates[0]][car_coordinates[1]] == '.':
            total_km += 10

    # print(car_coordinates)

matrix[car_coordinates[0]][car_coordinates[1]] = 'C'

if flag_F:
    print(f'Racing car {car_num} finished the stage!')
else:
    print(f'Racing car {car_num} DNF.')

print(f'Distance covered {total_km} km.')

for row in matrix:
    print(f'{"".join(row)}')
