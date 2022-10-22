# 20221007 - Python - Python Advanced - Workshop 2
# 01 - Console Tic Tac Toe


# _______________ version 2 _________________


from pyfiglet import Figlet             # big, slant, doom, standard, graffiti, cyberlarge
from colorama import Fore


def check_for_win(move=0):
    fig = Figlet(font)

    player_name, player_symbol = players[0]
    size = len(board)

    first_diagonal_win = all([board[i][i] == player_symbol for i in range(size)])
    second_diagonal_win = all([board[i][size - 1 - i] == player_symbol for i in range(size)])
    row_win = any(all(True if pos == player_symbol else False for pos in row) for row in board)
    col_win = any([all(True if board[r][c] == player_symbol else False for r in range(size)) for c in range(size)])

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print(Fore.LIGHTYELLOW_EX + fig.renderText(f'{player_name} won!'))
        print_board()
        raise SystemExit

    players.append(players.pop(0))


def place_symbol(position, move):
    row, col = (position - 1) // 3, (position - 1) % 3
    board[row][col] = players[0][1]
    move += 1

    check_for_win()
    if move == 9:
        print_board()
        print('No one wins! Play again!')
        raise SystemExit
    print_board()
    choose_position(move)


def choose_position(move):
    print()
    while True:
        try:
            position = int(input(f'{players[0][0]}, your turn now: '))
            print()
        except ValueError:
            print(f'\n{players[0][0]}, select a number in the range [1 - 9] and make sure it is not taken!\n')
            continue

        row, col = (position - 1) // 3, (position - 1) % 3
        if board[row][col] in [players[0][1], players[1][1]]:
            print('This position is already taken. Choose another position!\n')
            continue

        if 1 <= position <= len(board) * len(board):
            place_symbol(int(position), move)
            break
        else:
            print(f'\n{players[0][0]}, please select a valid position [1 - 9]!\n')


def print_board(begin=False):
    if begin:
        print('This is the numeration of the board:\n')
        [print(f'| {" | ".join(row)} |') for row in board]
        print(f'\n{players[0][0]} starts first!')

        for row in range(len(board)):
            for col in range(len(board)):
                board[row][col] = '_'
    else:
        [print(f'|  {"  |  ".join(row)}  |') for row in board]


def start():
    move = 0
    fig = Figlet(font)
    print(Fore.LIGHTYELLOW_EX + fig.renderText('Tic Tac Toe') + Fore.RESET)

    player_1_name = input('\nEnter a name for player 1: ').upper()
    player_2_name = input('Enter a name for player 2: ').upper()

    while True:
        player_1_symbol = input(f'\n{player_1_name}, choose your symbol: "X" or "O" ?').upper()

        if player_1_symbol not in ['X', 'O']:
            print(f'\n{player_1_name}, please select a valid option: "X" or "O"!')
        else:
            break

    player_2_symbol = "O" if player_1_symbol == 'X' else 'X'

    players.append([player_1_name, player_1_symbol])
    players.append([player_2_name, player_2_symbol])

    print_board(begin=True)
    choose_position(move)


players = []
board = [[str(i), str(i + 1), str(i + 2)]for i in range(1, 10, 3)]
font = 'doom'    # big, slant, doom, standard, graffiti, cyberlarge

start()


# _______________ version 1 _______________


# The board stays with number positions for the free cells.


def check_for_win():
    player_name, player_symbol = players[0]
    size = len(board)

    first_diagonal_win = all([board[i][i] == player_symbol for i in range(size)])
    second_diagonal_win = all([board[i][size - 1 - i] == player_symbol for i in range(size)])
    row_win = any(all(True if pos == player_symbol else False for pos in row) for row in board)
    col_win = any([all(True if board[r][c] == player_symbol else False for r in range(size)) for c in range(size)])

    if any([first_diagonal_win, second_diagonal_win, row_win, col_win]):
        print(f'\n{player_name} won!')
        print_board()
        raise SystemExit

    players.append(players.pop(0))


def place_symbol(position):
    row, col = (position - 1) // 3, (position - 1) % 3
    board[row][col] = players[0][1]

    check_for_win()
    print_board()
    choose_position()


def choose_position():
    print()
    while True:
        position = input(f'{players[0][0]} choose free position [1 - 9]')

        if any([True if position in row else False for row in board]):
            break
        else:
            print(f'{players[0][0]}, please select a valid position!')

    place_symbol(int(position))
    check_for_win()


def print_board(begin=False):
    print()
    if begin:
        print('This is the numeration of the board:\n')
        [print(f'| {" | ".join(row)} |') for row in board]
        print(f'\n{players[0][0]} starts first!')
    else:
        [print(f'| {" | ".join(row)} |') for row in board]


def start():
    player_1_name = input('\nEnter a name for player 1: ')
    player_2_name = input('Enter a name for player 2: ')

    while True:
        player_1_symbol = input(f'\n{player_1_name}, choose your symbol: "X" or "O" ?').upper()

        if player_1_symbol not in ['X', 'O']:
            print(f'\n{player_1_name}, please select a valid option: "X" or "O"')
        else:
            break

    player_2_symbol = "O" if player_1_symbol == 'X' else 'X'

    players.append([player_1_name, player_1_symbol])
    players.append([player_2_name, player_2_symbol])

    print_board(begin=True)
    choose_position()


players = []
board = [[str(i), str(i + 1), str(i + 2)]for i in range(1, 10, 3)]

start()
