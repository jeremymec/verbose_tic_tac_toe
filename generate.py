from copy import deepcopy

def print_board(board):
    print("----")
    print(board[0][0], board[0][1], board[0][2])
    print(board[1][0], board[1][1], board[1][2])
    print(board[2][0], board[2][1], board[2][2])
    print("----")

def next_move(move):
    if (move == 'X'):
        return 'Y'
    if (move == 'Y'):
        return 'X'
    raise Exception("Waaweewaa that is not move!")

board = [[0 for x in range(3)] for y in range(3)]

counter = 0

def it():
    global counter
    counter = 0
    for y in range(3):
        for x in range(3):
            iterate(deepcopy(board), x, y, 'X', 0)


def iterate(board, move_x, move_y, move_val, depth):
    board[move_y][move_x] = move_val
    global counter
    print_board(board)
    print(depth)
    terminal = True
    for y in range(3):
        for x in range(3):
            if (board[y][x] == 0):
                terminal = False
                iterate(deepcopy(board), x, y, next_move(move_val), depth + 1)
    if terminal:
        counter = counter + 1


it()

print(counter)