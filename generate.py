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
    raise Exception("Waaweewaa that is not move!")

board = [[0 for x in range(3)] for y in range(3)]

input_statement = '{indent}move = input("Enter your move")'
if_statement = '{indent}if (move == "{y},{x}"):'
print_board_statement = '{indent}print("{board_string}")'

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
    print(print_board_statement.format(indent='  ' * (depth), board_string=print_board(board)))
    print(input_statement.format(indent='  ' * (depth)))

    for y in range(3):
        for x in range(3):
            if (board[y][x] == 0):
                # terminal = False
                iterate(deepcopy(board), x, y, next_move(move_val), depth + 1)
    # if terminal:
    #     counter = counter + 1


it()

print(counter)