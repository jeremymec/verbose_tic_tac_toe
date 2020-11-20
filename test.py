from goto import with_goto

@with_goto
def play():
    player_one_move = input("Player one: enter the coords of your move")
    if (player_one_move == "0,0"):
        label .p100
        player_two_move = input("Player two: enter the coords of your move")
        if (player_two_move == "0,0"):
            print("That square is already taken")
            goto .p100
        if (player_two_move == "0,1"):
            label .p100p201
            player_one_move = input("Player one: enter the coords of your move")
            if (player_one_move == "0,0"):
                print("That square is already taken")
                goto .p100p201
            if (player_one_move == "0,1"):
                print("That square is already taken")
                goto .p100p201
            if (player_one_move == "1,1"):
                print("done")






play()