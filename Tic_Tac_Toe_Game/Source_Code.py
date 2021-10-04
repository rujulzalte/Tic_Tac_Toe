# This is a simple code for the game Tic Tac Toe
# You can play with computer
# Code is implemented on basic knowledge of While loop, Function and if else

import random


def main_tic_tac_toe():
    def instructions():
        print(""" **WELCOME TO THE**\n
 ________   _   ______             _________   ______    ______             _________    _______    ________
/___  ___\ / \ /   ___/           /___   ___\ /  __  \  /  ____/           /___   ___\  /  ___  \  /   _____\
   / \     | | |  /       _____       / \     |  __  | |  /        ______      / \     |  /   \  | |   \
   | |     | | |  \___    \_____\     | |     | |  | | |  \____    \_____\     | |     |  \___/  | |   /____
   \_/     \_/ \______\               \_/     \_/  \_/  \______\               \_/      \_______/   \________\
   \n\n **GAME** CODED BY: RUJUL ZALTE    \n
    THIS WILL BE A BATTLE BETWEEN A HUMAN MIND \
AND AN ARTIFICIAL INTELLIGENCE(COMPUTER)	\n
    BOARD WOULD LOOK SIMILAR TO THIS & ENSURE \
THAT YOU MENTION NUMBERS WITHIN RANGE 0-8:\n\n
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8			\n
    """)

    instructions()

    ttt_Board = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # Creating Dummy Board

    def display_board(ttt_Board):  # Display board function definition
        print (" ____________")
        print ("||", ttt_Board[0], "||", ttt_Board[1], "||", ttt_Board[2])
        print (" ____________")
        print ("||", ttt_Board[3], "||", ttt_Board[4], "||", ttt_Board[5])
        print (" ____________")
        print ("||", ttt_Board[6], "||", ttt_Board[7], "||", ttt_Board[8])
        print (" ____________")
    display_board(ttt_Board)

    # Chance given to Player to enter the choice
    def choose_player(ttt_Board, user_char):
        valid_move = False
        while (not valid_move):
            if user_char == "X":
                choice = int(input("PLAYER: PLEASE SELECT YOUR CHOICE \
TO MAKE A MOVE ON THE BOARD: \n >> "))
                if choice in range(0, 9):
                    if (ttt_Board[choice] != "X" and ttt_Board[choice] != "O"):
                        ttt_Board[choice] = "X"
                        valid_move = True
                    else:
                        print("SORRY THE POSTION IS ALREADY \
OCCUPIED BY :, ", ttt_Board[choice])
                else:
                    print("SORRY WRONG INPUT (PLEASE MENTION BETWEEN 0-8)")
            elif user_char == "O":
                choice = int(input("PLAYER: PLEASE SELECT YOUR CHOICE \
TO MAKE A MOVE ON THE BOARD: \n >> "))
                if choice in range(0, 9):
                    if (ttt_Board[choice] != "X" and ttt_Board[choice] != "O"):
                        ttt_Board[choice] = "O"
                        valid_move = True
                    else:
                        print("SORRY THE POSTION IS ALREADY \
OCCUPIED BY :, ", ttt_Board[choice])
                else:
                    print("SORRY WRONG INPUT (PLEASE MENTION BETWEEN 0-8)")
        return win_direction(ttt_Board)

    # Chance given to Computer to enter the choice
    def choose_computer(ttt_board, user_char):
        valid_move = False
        if user_char == "X":
            while (not valid_move):
                random.seed()
                choice = random.randint(0, 8)
                if (ttt_Board[choice] != "X" and ttt_Board[choice] != "O"):
                    ttt_Board[choice] = "O"
                    print("COMPUTER MADE THE MOVE")
                    valid_move = True
        elif user_char == "O":
            while (not valid_move):
                random.seed()
                choice = random.randint(0, 8)
                if (ttt_Board[choice] != "X" and ttt_Board[choice] != "O"):
                    ttt_Board[choice] = "X"
                    print("COMPUTER MADE THE MOVE")
                    valid_move = True
        return win_direction(ttt_Board)

    # Deciding the Vertical Winning Conditions
    def win_vertical(ttt_board):
        winner = False
        if (ttt_Board[0] == ttt_Board[3] == ttt_Board[6]):
            winner = True
        elif (ttt_Board[1] == ttt_Board[4] == ttt_Board[7]):
            winner = True
        elif (ttt_Board[2] == ttt_Board[5] == ttt_Board[8]):
            winner = True
        return winner

    # Deciding the Horizontal Winning Conditions
    def win_horizontal(ttt_board):
        winner = False
        if (ttt_Board[0] == ttt_Board[1] == ttt_Board[2]):
            winner = True
        elif (ttt_Board[3] == ttt_Board[4] == ttt_Board[5]):
            winner = True
        elif (ttt_Board[6] == ttt_Board[7] == ttt_Board[8]):
            winner = True
        return winner

    # Deciding the Diagonal Winning Conditions
    def win_diagonal(ttt_board):
        winner = False
        if (ttt_Board[0] == ttt_Board[4] == ttt_Board[8]):
            winner = True
        elif (ttt_Board[2] == ttt_Board[4] == ttt_Board[6]):
            winner = True
        return winner

    # Which Direction you won the game
    def win_direction(ttt_board):
        game_winner = False
        if (win_vertical(ttt_board) == True):
            game_winner = True
        elif (win_horizontal(ttt_board) == True):
            game_winner = True
        elif (win_diagonal(ttt_board) == True):
            game_winner = True
        return game_winner

    # DECIDE TO RESTART THE GAME
    def restart():
        print("DO YOU WANT TO RESTART THE AGAIN ? (Y/N) \n>>")
        re = input()
        re = re.upper()
        if(re == "Y"):
            main_tic_tac_toe()
        elif(re == "N"):
            print("THANK YOU FOR PLAYING THE GAME")
            exit(0)
        else:
            print("INVALID INPUT PLEASE ENTER (Y/N)")
            restart()

    # DECISION MAKING ON WHO SHOULD START THE GAME
    start = input("DO YOU LIKE START THE GAME HERE: (Y/N) \n>> ")
    start = start.upper()
    x = True
    while x:
        if start == "Y":
            print("GREAT YOU ARE THE ONE \
WHO IS GOING TO GO FIRST:  ")
            x = False
        elif start == "N":
            print("AS YOU DECIDED TO NOT START FIRST, \
GIVING COMPUTER THE FIRST MOVE:  ")
            x = False
        else:
            print("INVALID INPUT PLEASE ENTER (Y/N)")
            start = input("DO YOU LIKE START THE GAME HERE: (Y/N) \n>> ")
            start = start.upper()

    # TAKING VALUE FROM USER
    user_char = input("CHOOSE THE CHARATER YOU WANT \
TO PLAY WITH (X/O) \n>>")
    user_char = user_char.upper()

    # DECIDE THE ALTERNATE CHANCES
    turn = 0
    won = False
    while (not won and turn < 9):
        if start == "Y":
            if turn % 2 == 0:
                won = choose_player(ttt_Board, user_char)
            else:
                won = choose_computer(ttt_Board, user_char)
            turn = turn + 1
            display_board(ttt_Board)

        if start == "N":
            if turn % 2 == 0:
                won = choose_computer(ttt_Board, user_char)
            else:
                won = choose_player(ttt_Board, user_char)
            turn = turn + 1
            display_board(ttt_Board)

    print(turn)
    turn = turn - 1

    if (not won):
        print("HELLO IT IS A TIE!!!")
        restart()
    if start == "Y":
        if turn % 2 == 0 and (won):
            print("CONGRATULATIONS !!!! YOU WON THE GAME")
        elif won:
            print("COMPUTER AGAIN DID IT, AND WON THE GAME")
        restart()
    if start == "N":
        if turn % 2 == 0 and (won):
            print("COMPUTER AGAIN DID IT, AND WON THE GAME")
        elif won:
            print("CONGRATULATIONS !!!! YOU WON THE GAME")
        restart()

main_tic_tac_toe()
