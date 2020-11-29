from copy import deepcopy

def print_board(board):
    board_string = ""
    board_string += "----\\n"
    board_string += (str(board[0][0]) + str(board[0][1]) + str(board[0][2]) + '\\n')
    board_string += (str(board[1][0]) + str(board[1][1]) + str(board[1][2]) + '\\n')
    board_string += (str(board[2][0]) + str(board[2][1]) + str(board[2][2]) + '\\n')
    board_string += "----\\n"
    return board_string

def next_move(move):
    if (move == 'X'):
        return 'Y'
    if (move == 'Y'):
        return 'X'

def check_win(board):
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            return board[0][i]
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            return board[i][0]
    
    if board[0][0] == board[1][1] and board[1][1] == board [2][2]:
        return board[0][0]

    if board[2][0] == board[1][1] and board[1][1] == board [0][2]:
        return board[2][0]

    return 0


board = [[0 for x in range(3)] for y in range(3)]

input_statement = '{indent}move = input("Enter your move")'
if_statement = '{indent}if (move == "{y},{x}"):'
print_board_statement = '{indent}print("{board_string}")'
game_over_statemet = '{indent}print(\"Game Over. {player} Wins.\")'
finish_game_statement = '{indent}exit()'

def it():
    global counter
    counter = 0
    print(input_statement.format(indent=''))
    for y in range(3):
        for x in range(3):
            iterate(deepcopy(board), x, y, 'X', 1)


def iterate(board, move_x, move_y, move_val, depth):
    if (depth > 8): return
    print(if_statement.format(indent='  ' * (depth - 1), y=move_y, x=move_x))
    board[move_y][move_x] = move_val
    win = check_win(board)
    if (win != 0):
        print(game_over_statemet.format(indent='  ' * depth, player=win))
        print(finish_game_statement.format(indent='  ' * depth))
        return
    print(print_board_statement.format(indent='  ' * (depth), board_string=print_board(board)))
    print(input_statement.format(indent='  ' * (depth)))

    for y in range(3):
        for x in range(3):
            if (board[y][x] == 0):
                iterate(deepcopy(board), x, y, next_move(move_val), depth + 1)

it()

print(counter)