# This is main program for Snake & Ladder
# We need to have Players (place to save their position),
# We need to have Dice function to generate random 1 ~ 6 (Presently it is an input)
# We need to have standard as well as custom built board
# [Board has 1 to 100 box and has Snake on certain boxes while
# ladder on certain other boxes.]
# Lets make game with 4 players P1 to P4,
# Should we try making it for n number
# of players ?
P1 = 0
P2 = 0
P3 = 0
P4 = 0
def check_board(n):
    #this dictionary is the built_in Board, from key we jump to values
    board = {4: 14, 9: 30, 20: 38, 25: 3, 28 : 84, 36: 44, 42: 63, 51: 67, 56: 48, 59: 1, 62: 81, 69: 32, 71: 90, 83: 57, 91: 73, 94: 26, 99: 80,}
    if board.has_key(n):
        print "You have to Jump" # Need to check if P1 has landed on Snake or is climbing ladder
        if n > board[n]:
            print "Its a Snake . . . ."
        else:
            print "Climb The Ladder . . . ."
        n = board[n]
    return n
def print_status():
    print "  "
    print "Current Status : "
    print "  P1", P1, "\tP2", P2
    print "  P3", P3, "\tP4", P4
    print "  "
    return
def roll_dice(r):
    d = input("What does Dice Say ?")
    while d < 1 or d > 6:
        d = input("check your Dice it should show 1 to 6 ?")
    d = r + d
    return d
while P1 < 100 or P2 < 100 or P3 < 100 or P4 < 100:
        print "Its turn of Player P1",
        P1 = roll_dice(P1)
        P1 = check_board(P1)
        print_status()
        if P1 > 99:
            print "we have a winner and its P1"
            break
        print "Its turn of Player P2",
        P2 = roll_dice(P2)
        P2 = check_board(P2)
        print_status()
        if P2 > 99:
            print "we have a winner and its P2"
            break
        print "Its turn of Player P3",
        P3 = roll_dice(P3)
        P3 = check_board(P3)
        print_status()
        if P3 > 99:
            print "we have a winner and its P3"
            break
        print "Its turn of Player P4",
        P4 = roll_dice(P4)
        P4 = check_board(P4)
        print_status()
        if P4 > 99:
            print "we have a winner and its P4"
            break
　
