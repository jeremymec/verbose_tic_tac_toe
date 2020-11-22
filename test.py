from goto import with_goto

@with_goto
def play():
    move = input("Enter your move)
    if (move == "0,0"):
        label .p100
        move = input("Player two: enter the coords of your move")
        if (move == "0,0"):
            print("That square is already taken")
            goto .p100
        if (move == "0,1"):
            label .p100p201
            move = input("Enter your move)
            if (move == "0,0"):
                print("That square is already taken")
                goto .p100p201
            if (move == "0,1"):
                print("That square is already taken")
                goto .p100p201
            if (move == "1,1"):
                print("done")






play()