# 20221006 - Python - Python Advanced - Workshop 1
# 01 - Console Connect Four


# _______________ version 1 _______________

from collections import deque
from colorama import Fore


player_1_symbol = 'A'
player_2_symbol = 'B'
empty_cell_symbol = '.'

rows, cols = 6, 7

turn = deque([player_1_symbol, player_2_symbol])
board = [[empty_cell_symbol] * cols for row in range(rows)]

directions = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (-1, -1),
    (-1, 1),
    (1, 1),
    (1, -1)
)

# Game main loop
while True:
    print()
    [print(f'[ {" ".join(row)} ]') for row in board]
    player_symbol = turn[0]

    # Selecting the correct entry for column
    try:
        player_col_i = int(input(f'\nPlayer {player_symbol}, please choose a column: ')) - 1
    except ValueError:
        print(f'Select a valid entry! Number in the range ({1} - {cols})')
        continue

    if not 0 <= player_col_i < cols:
        print(Fore.LIGHTRED_EX + f'Select a number in the range ({1} - {cols})' + Fore.RESET)
        continue

    # Testing the selected column for empty cells
    row_i = 0

    if board[row_i][player_col_i] != empty_cell_symbol:
        print(Fore.LIGHTRED_EX + '\nNo empty spaces on that row!\nEnter a different row.' + Fore.RESET)
        continue

    while True:
        if row_i == rows - 1 or board[row_i + 1][player_col_i] != empty_cell_symbol:
            board[row_i][player_col_i] = player_symbol
            break

        row_i += 1

    # Checking the whole board for winning configuration (from (0, 0) to (max row, max col))
    for row in range(rows):
        for col in range(cols):
            if board[row][col] != player_symbol:
                continue

            # It takes every pair of coordinates  and...
            for coordinates in directions:
                r, c = row, col

                # ... tests 3 cells in every direction searching for 4 consecutive
                for _ in range(3):
                    r += coordinates[0]
                    c += coordinates[1]

                    if not (0 <= r < rows and 0 <= c < cols):
                        break

                    if board[r][c] != player_symbol:
                        break

                # When the winner is found!
                else:
                    print()
                    [print(f'[ {" ".join(row)} ]') for row in board]
                    print(Fore.LIGHTBLUE_EX + f'\nThe winner is Player: {player_symbol}' + Fore.RESET)
                    raise SystemExit

    turn.append(turn.popleft())


# _______________ version 2 ____________ w/functions and recursion (just for illustration) _______

from collections import deque
from colorama import Fore


def place_symbol(row_i):
    if row_i == rows - 1 or board[row_i + 1][player_col_i] != empty_cell_symbol:
        board[row_i][player_col_i] = player_symbol
        return
    place_symbol(row_i + 1)


def check_for_win(r, c, coordinates, iterations):
    if not (0 <= r < rows and 0 <= c < cols):
        return False

    if board[r][c] != player_symbol:
        return False

    if iterations == 3:
        print()
        [print(f'[ {" ".join(row)} ]') for row in board]
        print(Fore.LIGHTRED_EX + '\nThe winner is Player: {player_symbol}')
        return True

    return check_for_win(r + coordinates[0], c + coordinates[1], coordinates, iterations + 1)


player_1_symbol = 'A'
player_2_symbol = 'B'
empty_cell_symbol = '.'

rows, cols = 6, 7

turn = deque([player_1_symbol, player_2_symbol])
board = [[empty_cell_symbol] * cols for row in range(rows)]
win = False

directions = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1),
    (-1, -1),
    (-1, 1),
    (1, 1),
    (1, -1)
)

# Game main loop
while not win:
    print()
    [print(f'[ {" ".join(row)} ]') for row in board]
    player_symbol = turn[0]

    try:
        player_col_i = int(input(f'\nPlayer {player_symbol}, please choose a column: ')) - 1
    except ValueError:
        print(f'Select a valid entry! Number in the range ({1} - {cols})')
        continue

    if not 0 <= player_col_i < cols:
        print(f'Select a number in the range ({1} - {cols})')
        continue

    row_i = 0

    if board[row_i][player_col_i] != empty_cell_symbol:
        print('\nNo empty spaces on that row!\nEnter a different row.')
        continue

    place_symbol(row_i)

    # Checking the whole board for winning configuration (from (0, 0) to (max row, max col))
    for row in range(rows):
        for col in range(cols):
            if board[row][col] != player_symbol:
                continue

            for coordinates in directions:
                win = check_for_win(row + coordinates[0], col + coordinates[1], coordinates, 1)
                if win:
                    break
            if win:
                break
        if win:
            break

    turn.append(turn.popleft())
