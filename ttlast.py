import string
import time
import copy
import os
import random
from itertools import chain
from operator import itemgetter
import sys
from termcolor import colored, cprint
import math

from math import inf as infinity
import platform
from random import choice


HUMAN = -1
COMP = +1
board1 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]
board2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]


def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
def init_board():
    """Returns an empty 3-by-3 board (with zeros)."""
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    return board

def init_board5():
    """Returns an empty 3-by-3 board (with zeros)."""
    board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    return board

def get_move5(board, player,used_letters, mode):


    row, col = 0, 0
    coordinates = (
    "A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5", "C1", "C2", "C3", "C4", "C5", "D1", "D2", "D3", "D4",
    "D5", "E1", "E2", "E3", "E4", "E5")
    print("\n Your turn: ", player)
    coordinate = str.upper(input("Please choose a cordinate: "))
    if coordinate == "QUIT":
        print("You quit")
        exit()
    while coordinate not in coordinates:
        os.system("clear")
        print_board5(board, mode)
        print("invalid character!")
        coordinate = str.upper(input("Pleas choose a cordinate: "))
        if coordinate == "QUIT":
            print("you quit")
            exit()
    while coordinate in used_letters:
        os.system("clear")
        print_board5(board, mode)
        print("you used that please choose an other one.")
        coordinate = str.upper(input("Pleas choose a cordinate: "))
        while coordinate not in coordinates:
            print("invalid character!")
            coordinate = str.upper(input("Pleas choose a cordinate: "))

    used_letters.append(coordinate)

    for i in range(len(coordinate)):
        if i == 0:
            row = coordinate[i]
    for i in range(len(coordinate)):
        if i == 1:
            col = coordinate[i]
    col = int(col)
    col -= 1

    if row == "A":
        row = 0
    elif row == "B":
        row = 1
    elif row == "C":
        row = 2
    elif row == "D":
        row = 3
    elif row == "E":
        row = 4

    # new_board = copy.copy(board)
    # new_board[row][col] = player

    return row, col

def get_ai_move5(board, player, used_letters):

    row = 0
    col = 0

    while board[row][col] != '.':
        row = random.randint(0, 4)
        col = random.randint(0, 4)
    a = row
    b = col
    if a == 0:
        a = "A"
    elif a == 1:
        a = "B"
    elif a == 2:
        a = "C"
    elif a == 3:
        a = "D"
    elif a == 4:
        a = "E"
    b += 1
    b = str(b)
    ai_letter = a + b
    used_letters.append(ai_letter)
    return (row, col)

def is_full5(board):

    count = 0
    for i in range(len(board)):
        for y in range(len(board)):
            if board[i][y] != ".":
                count += 1

                if count == 25:
                    return True

    return False

def print_board5(board, mode):
    print(""" """)
    prCyan("     " + mode)
    print(""" """)

    print("        1     2     3     4     5")
    print("     -------------------------------")
    print('A    |  ' + str(colored(board[0][0])) + '  |  ' + str(colored(board[0][1])) + '  |  ' + str(colored(board[0][2])) + '  |  ' + str(colored(board[0][3])) + '  |  ' + str(colored(board[0][4])) + '  |')
    print('     |-----+-----+-----+-----+-----|')
    print('B    |  ' + str(colored(board[1][0])) + '  |  ' + str(colored(board[1][1])) + '  |  ' + str(colored(board[1][2])) + '  |  ' + str(colored(board[1][3])) + '  |  ' + str(colored(board[1][4])) + '  |')
    print('     |-----+-----+-----+-----+-----|')
    print('C    |  ' + str(colored(board[2][0])) + '  |  ' + str(colored(board[2][1])) + '  |  ' + str(colored(board[2][2])) + '  |  ' + str(colored(board[2][3])) + '  |  ' + str(colored(board[2][4])) + '  |')
    print('     |-----+-----+-----+-----+-----|')
    print('D    |  ' + str(colored(board[3][0])) + '  |  ' + str(colored(board[3][1])) + '  |  ' + str(colored(board[3][2])) + '  |  ' + str(colored(board[3][3])) + '  |  ' + str(colored(board[3][4])) + '  |')
    print('     |-----+-----+-----+-----+-----|')
    print('E    |  ' + str(colored(board[4][0])) + '  |  ' + str(colored(board[4][1])) + '  |  ' + str(colored(board[4][2])) + '  |  ' + str(colored(board[4][3])) + '  |  ' + str(colored(board[4][4])) + '  |')
    print("     -------------------------------")


def has_won5(board, player):

    win_board = [
        [board[0][0], board[0][1], board[0][2], board[0][3], board[0][4]],
        [board[1][0], board[1][1], board[1][2], board[1][3], board[1][4]],
        [board[2][0], board[2][1], board[2][2], board[2][3], board[2][4]],
        [board[3][0], board[3][1], board[3][2], board[3][3], board[3][4]],
        [board[4][0], board[4][1], board[4][2], board[4][3], board[4][4]],
        [board[0][0], board[1][0], board[2][0], board[3][0], board[4][0]],
        [board[0][1], board[1][1], board[2][1], board[3][1], board[4][1]],
        [board[0][2], board[1][2], board[2][2], board[3][2], board[4][2]],
        [board[0][3], board[1][3], board[2][3], board[3][3], board[4][3]],
        [board[0][4], board[1][4], board[2][4], board[3][4], board[4][4]],
        [board[0][0], board[1][1], board[2][2], board[3][3], board[4][4]],
        [board[4][0], board[3][1], board[2][2], board[1][3], board[0][4]],
    ]
    if [player, player, player, player, player] in win_board:
        return True
    else:
        return False


def get_move(board, player,used_letters, mode):
    """Returns the coordinates of a valid move for player on board."""

    row, col = 0, 0
    coordinates = ("A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3")
    print("\n Your turn: ", player)
    coordinate = str.upper(input("Please choose a cordinate: "))
    if coordinate == "QUIT":
        print("You quit")
        exit()
    while coordinate not in coordinates:
        os.system("clear")
        print_board(board, mode)
        print("invalid character!")
        coordinate = str.upper(input("Pleas choose a cordinate: "))
        if coordinate == "QUIT":
            print("You quit")
            exit()
    while coordinate in used_letters:
        os.system("clear")
        print_board(board, mode)
        print("you used that please choose an other one.")
        coordinate = str.upper(input("Pleas choose a cordinate: "))
        while coordinate not in coordinates:
            print("invalid character!")
            coordinate = str.upper(input("Pleas choose a cordinate: "))

    used_letters.append(coordinate)

    for i in range(len(coordinate)):
        if i == 0:
            row = coordinate[i]
    for i in range(len(coordinate)):
        if i == 1:
            col = coordinate[i]
    col = int(col)
    col -= 1

    if row == "A":
        row = 0
    elif row == "B":
        row = 1
    elif row == "C":
        row = 2


    #new_board = copy.copy(board)
   # new_board[row][col] = player

    return row,col

def get_ai_move_medium(board, player, used_letters):
        row = 0
        col = 0

        while board[row][col] != '.':
            if board[0][0] == player and board[0][1] == player:
                if board[0][2] == '.':
                    row = 0
                    col = 2
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)

            elif board[1][0] == player and board[1][1] == player:
                if board[1][2] == '.':
                    row = 1
                    col = 2
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)

            elif board[2][0] == player and board[2][1] == player:
                if board[2][2] == '.':
                    row = 2
                    col = 2
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)

            elif board[0][0] == player and board[1][0] == player:
                if board[2][0] == '.':
                    row = 2
                    col = 0
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)

            elif board[0][1] == player and board[1][1] == player:
                if board[2][1] == '.':
                    row = 2
                    col = 1
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)

            elif board[0][2] == player and board[1][2] == player:
                if board[2][2] == '.':
                    row = 2
                    col = 2
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)

            elif board[0][0] == player and board[1][1] == player:
                if board[2][2] == '.':
                    row = 2
                    col = 2
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)

            elif board[0][2] == player and board[1][1] == player:
                if board[2][0] == '.':
                    row = 2
                    col = 0
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)

            elif board[0][0] == player and board[0][2] == player:
                if board[0][1] == '.':
                    row = 0
                    col = 1
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)

            elif board[1][0] == player and board[1][2] == player:
                if board[1][1] == '.':
                    row = 1
                    col = 1
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)

            elif board[2][0] == player and board[2][2] == player:
                if board[2][1] == '.':
                    row = 2
                    col = 1
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)

            elif board[0][0] == player and board[2][2] == player:
                if board[1][1] == '.':
                    row = 1
                    col = 1
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)

            elif board[2][0] == player and board[0][2] == player:
                if board[1][1] == '.':
                    row = 1
                    col = 1
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)

            elif board[2][0] == player and board[1][1] == player:
                if board[0][2] == '.':
                    row = 0
                    col = 2
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)

            elif board[2][2] == player and board[1][2] == player:
                if board[0][2] == '.':
                    row = 0
                    col = 2
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)

            elif board[2][2] == player and board[0][2] == player:
                if board[1][2] == '.':
                    row = 1
                    col = 2
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)

            elif board[2][2] == player and board[2][1] == player:
                if board[2][0] == '.':
                    row = 2
                    col = 0
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)

            elif board[1][2] == player and board[1][1] == player:
                if board[1][0] == '.':
                    row = 1
                    col = 0
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)

            elif board[0][2] == player and board[0][1] == player:
                if board[0][0] == '.':
                    row = 0
                    col = 0
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)

            elif board[2][2] == player and board[1][2] == player:
                if board[0][2] == '.':
                    row = 0
                    col = 2
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)
            elif board[2][1] == player and board[1][1] == player:
                if board[0][1] == '.':
                    row = 0
                    col = 1
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)
            elif board[1][2] == player and board[1][1] == player:
                if board[1][0] == '.':
                    row = 1
                    col = 0
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)
            elif board[0][0] == player and board[2][0] == player:
                if board[1][0] == '.':
                    row = 1
                    col = 0
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)
            elif board[2][0] == player and board[2][2] == player:
                if board[2][1] == '.':
                    row = 2
                    col = 1
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)
            elif board[2][1] == player and board[0][1] == player:
                if board[1][1] == '.':
                    row = 1
                    col = 1
                else:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)

            else:
                row = random.randint(0, 2)
                col = random.randint(0, 2)

        a = row
        b = col
        if a == 0:
            a = "A"
        elif a == 1:
            a = "B"
        elif a == 2:
            a = "C"
        b += 1
        b = str(b)
        ai_letter = a + b
        used_letters.append(ai_letter)

        return (row, col)


def get_ai_move(board, player, used_letters):

    row = 0
    col = 0

    while board[row][col] != '.':
        row = random.randint(0, 2)
        col = random.randint(0, 2)
    a = row
    b = col
    if a == 0:
        a = "A"
    elif a == 1:
        a = "B"
    elif a == 2:
        a = "C"
    b += 1
    b = str(b)
    ai_letter = a + b
    used_letters.append(ai_letter)
    return (row, col)




def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    new_board = copy.copy(board)
    new_board[row][col] = player

    return row,col



def has_won(board, player):
    """Returns True if player has won the game."""

    # Check all possible winning combinations

    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return True
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return True
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return True
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return True
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return True
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return True
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    elif board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    else:
        return False



def is_full(board):
    """Returns True if board is full."""

    count = 0
    for i in range(len(board)):
        for y in range(len(board)):
            if board[i][y] != ".":
                count += 1

                if count == 9:
                    return True

    return False



def print_board(board, mode):
    print(""" """)
    prCyan("     " + mode)
    print(""" """)

    print("        1     2     3")
    print("     -------------------")
    print('A    |  ' + str(colored(board[0][0])) + '  |  ' + str(colored(board[0][1])) + '  |  ' + str(colored(board[0][2])) + '  |')
    print('     |-----+-----+-----|')
    print('B    |  ' + str(colored(board[1][0])) + '  |  ' + str(colored(board[1][1])) + '  |  ' + str(colored(board[1][2])) + '  |')
    print('     |-----+-----+-----|')
    print('C    |  ' + str(colored(board[2][0])) + '  |  ' + str(colored(board[2][1])) + '  |  ' + str(colored(board[2][2])) + '  |')
    print("     -------------------")
def print_result(player):
    """Congratulates winner or proclaims tie (if winner equals zero)."""

    if player == colored("X", 'blue'):
        cprint("""
        ██╗  ██╗    ██╗    ██╗██╗███╗   ██╗    
        ╚██╗██╔╝    ██║    ██║██║████╗  ██║    
         ╚███╔╝     ██║ █╗ ██║██║██╔██╗ ██║    
         ██╔██╗     ██║███╗██║██║██║╚██╗██║    
        ██╔╝ ██╗    ╚███╔███╔╝██║██║ ╚████║    
        ╚═╝  ╚═╝     ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝ 
        """, 'blue', attrs=['bold'], file=sys.stderr)
    if player == colored("O", 'red'):
        cprint("""
         ██████╗     ██╗    ██╗██╗███╗   ██╗
        ██╔═══██╗    ██║    ██║██║████╗  ██║
        ██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║
        ██║   ██║    ██║███╗██║██║██║╚██╗██║
        ╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║
         ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝
        """, 'red', attrs=['bold'], file=sys.stderr)
    exit()


def tic_tac_draw():
    cprint("""
      
                    ████████╗██╗ ██████╗
                    ╚══██╔══╝██║██╔════╝
                       ██║   ██║██║
                       ██║   ██║██║
                       ██║   ██║╚██████╗
                       ╚═╝   ╚═╝ ╚═════╝""", 'blue', attrs=['bold'], file=sys.stderr)
    cprint("""
                                         ████████╗ █████╗  ██████╗
                                         ╚══██╔══╝██╔══██╗██╔════╝
                                            ██║   ███████║██║
                                            ██║   ██╔══██║██║
                                            ██║   ██║  ██║╚██████╗
                                            ╚═╝   ╚═╝  ╚═╝ ╚═════╝""", 'yellow', attrs=['bold'], file=sys.stderr)
    cprint("""
                                                                    ████████╗ ██████╗ ███████╗
                                                                    ╚══██╔══╝██╔═══██╗██╔════╝
                                                                       ██║   ██║   ██║█████╗
                                                                       ██║   ██║   ██║██╔══╝
                                                                       ██║   ╚██████╔╝███████╗
                                                                       ╚═╝   ╚═╝  ╚═╝ ╚══════╝""", 'red', attrs=['bold'], file=sys.stderr)

def tie():
    cprint("""
        ██╗████████╗███████╗     █████╗     ████████╗██╗███████╗██╗
        ██║╚══██╔══╝██╔════╝    ██╔══██╗    ╚══██╔══╝██║██╔════╝██║
        ██║   ██║   ███████╗    ███████║       ██║   ██║█████╗  ██║
        ██║   ██║   ╚════██║    ██╔══██║       ██║   ██║██╔══╝  ╚═╝
        ██║   ██║   ███████║    ██║  ██║       ██║   ██║███████╗██╗
        ╚═╝   ╚═╝   ╚══════╝    ╚═╝  ╚═╝       ╚═╝   ╚═╝╚══════╝╚═╝""", 'yellow', attrs=['bold'], file=sys.stderr)
    exit()

def tictactoe_ai_medium(mode, choose):
    used_letters = []
    board = init_board()
    for i in range(len(board)):
        for y in range(len(board)):
            if board[i][y] == 0:
                board[i][y] = "."

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    characters = ("X", "x", "O", "o")
    player = str.upper(input("                           please choose and press X or O: "))
    if player == "QUIT":
        print("You quit")
        exit()
    while player not in characters:
        os.system("clear")
        tic_tac_draw()
        draw()
        print("                           Choose a game mode. Press a number from 1 to 8!: ", choose)
        print("""            
                                              invalid character
         """)
        player = str.upper(input("                           please choose and press X or O: "))
    if player == "X":
        i = colored(player, 'blue')
    else:
        i = colored(player, 'red')
    while has_won(board, player) != True and is_full(board) != True:
        os.system("clear")
        print_board(board, mode)
        print("\n used characters: ", end=" ")
        for letter in used_letters:

            print(letter + ", ", end=" ")
        player = i
        row, col = get_move(board, player,used_letters, mode)
        mark(board, player, row, col)
        if has_won(board, player) == True:
            os.system("clear")
            print_board(board, mode)
            print_result(player)
        is_full(board)
        if is_full(board) == True:
            os.system("clear")
            print_board(board, mode)
            print(tie())
        print_board(board, mode)
        if player == colored("O", 'red'):
            i = colored("X", 'blue')
        elif player == colored("X", 'blue'):
            i = colored("O", 'red')

        row, col = get_ai_move_medium(board, player, used_letters)
        player = i
        mark(board, player, row, col)
        has_won(board, player)
        if has_won(board, player) == True:
            os.system("clear")
            print_board(board, mode)
            print_result(player)
        is_full(board)
        if is_full(board) == True:
            os.system("clear")
            print_board(board, mode)
            print(tie())

        if player == colored("O", 'red'):
            i = colored("X", 'blue')
        elif player == colored("X", 'blue'):
            i = colored("O", 'red')

def tictactoe_ai(mode, choose):
    used_letters = []
    board = init_board()
    for i in range(len(board)):
        for y in range(len(board)):
            if board[i][y] == 0:
                board[i][y] = "."

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    characters = ("X", "x", "O", "o")
    player = str.upper(input("                           please choose and press X or O: "))
    if player == "QUIT":
        print("You quit")
        exit()
    while player not in characters:
        os.system("clear")
        tic_tac_draw()
        draw()
        print("                           Choose a game mode. Press a number from 1 to 8!: ", choose)
        print("""            
                                              invalid character
         """)
        player = str.upper(input("                           please choose and press X or O: "))
    if player == "X":
        i = colored(player, 'blue')
    else:
        i = colored(player, 'red')
    while has_won(board, player) != True and is_full(board) != True:
        os.system("clear")
        print_board(board, mode)
        print("\n used characters: ", end=" ")
        for letter in used_letters:

            print(letter + ", ", end=" ")
        player = i
        row, col = get_move(board, player,used_letters, mode)
        mark(board, player, row, col)
        if has_won(board, player) == True:
            os.system("clear")
            print_board(board, mode)
            print_result(player)
        is_full(board)
        if is_full(board) == True:
            os.system("clear")
            print_board(board, mode)
            print(tie())
        print_board(board, mode)
        if player == colored("O", 'red'):
            i = colored("X", 'blue')
        elif player == colored("X", 'blue'):
            i = colored("O", 'red')
        player = i
        row, col = get_ai_move(board, player, used_letters)
        mark(board, player, row, col)
        has_won(board, player)
        if has_won(board, player) == True:
            os.system("clear")
            print_board(board, mode)
            print_result(player)
        is_full(board)
        if is_full(board) == True:
            os.system("clear")
            print_board(board, mode)
            print(tie())

        if player == colored("O", 'red'):
            i = colored("X", 'blue')
        elif player == colored("X", 'blue'):
            i = colored("O", 'red')


def tictactoe_game(mode, choose):

    used_letters = []
    board = init_board()
    for i in range(len(board)):
        for y in range(len(board)):
            if board[i][y] == 0:
                board[i][y] = "."

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    characters = ("X","x","O","o")
    player = str.upper(input("                           please choose and press X or O: "))
    if player == "QUIT":
        print("You quit")
        exit()
    while player not in characters:
        os.system("clear")
        tic_tac_draw()
        draw()
        print("                           Choose a game mode. Press a number from 1 to 8!: ", choose)
        print("""            
                                              invalid character
         """)
        player = str.upper(input("                           please choose and press X or O: "))
    if player == "X":
        i = colored(player, 'blue')
    else:
        i = colored(player, 'red')
    while has_won(board, player) != True and is_full(board) != True:
        os.system("clear")
        player = i
        print_board(board, mode)
        print("\n used characters: ", end=" ")
        for letter in used_letters:

            print(letter + ", ", end=" ")
      
        row, col = get_move(board, player,used_letters, mode)
        mark(board, player, row, col)
        has_won(board, player)
        if has_won(board, player) == True:
            os.system("clear")
            print_board(board, mode)
            print_result(player)
        is_full(board)
        if is_full(board) == True:
            os.system("clear")
            print_board(board, mode)
            print(tie())

        if player == colored("O", 'red'):
            i = colored("X", 'blue')
        elif player == colored("X", 'blue'):
            i = colored("O", 'red')

def ai_ai(mode):
    used_letters = []
    board = init_board()
    for i in range(len(board)):
        for y in range(len(board)):
            if board[i][y] == 0:
                board[i][y] = "."

    player = ("X")

    h = colored(player, 'blue')
    c = colored("O", 'red')
    while has_won(board, player) != True and is_full(board) != True:
        os.system("clear")
        player = h
        print_board(board, mode)
        print("Your turn: ", player)
        time.sleep(1)
        row, col = get_ai_move_medium(board, player, used_letters)
        mark_ai(player, row, col, h, c)
        mark(board, player, row, col)
        if has_won(board, player) == True:
            os.system("clear")
            print_board(board, mode)
            print_result(player)
        is_full(board)
        if is_full(board) == True:
            os.system("clear")
            print_board(board, mode)
            print(tie())

        player = c
        if player == colored("O", 'red'):
            os.system("clear")
            print_board(board, mode)
            print("Your turn: ", player)
            time.sleep(1)
            row, col = ai_turn(board, player, used_letters, c, h)
            mark_ai(player, row, col, h, c)
            mark(board, player, row, col)
            has_won(board, player)
        if has_won(board, player) == True:
            os.system("clear")
            print_board(board, mode)
            print_result(player)
        is_full(board)
        if is_full(board) == True:
            os.system("clear")
            print_board(board, mode)
            print(tie())



def ai_hard(mode, choose):

    used_letters = []
    board = init_board()
    for i in range(len(board)):
        for y in range(len(board)):
            if board[i][y] == 0:
                board[i][y] = "."

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    characters = ("X", "x", "O", "o")
    player = str.upper(input("                           please choose and press X or O: "))
    if player == "QUIT":
        print("You quit")
        exit()
    while player not in characters:
        os.system("clear")
        tic_tac_draw()
        draw()
        print("                           Choose a game mode. Press a number from 1 to 8!: ", choose)
        print("""            
                                             invalid character
        """)
        player = str.upper(input("                           please choose and press X or O: "))
    if player == "X":
        i = colored(player, 'blue')
    else:
        i = colored(player, 'red')
    h = i

    if h == colored("X", 'blue'):
        c = colored("O", 'red')
    else:
        c = colored("X", 'blue')
    while has_won(board, player) != True and is_full(board) != True:
        os.system("clear")
        print_board(board, mode)
        print("\n used characters: ", end=" ")
        for letter in used_letters:

            print(letter + ", ", end=" ")
        player = i
        row, col = get_move(board, player,used_letters, mode)
        mark_ai(player, row, col, h, c)
        mark(board, player, row, col)
        if has_won(board, player) == True:
            os.system("clear")
            print_board(board, mode)
            print_result(player)
        is_full(board)
        if is_full(board) == True:
            os.system("clear")
            print_board(board, mode)
            print(tie())
       
        if player == colored("O", 'red'):
            i = colored("X", 'blue')
        elif player == colored("X", 'blue'):
            i = colored("O", 'red')
        player = i
        row, col = ai_turn(board, player, used_letters, c, h)
        mark_ai(player, row, col, h, c)
        mark(board, player, row, col)
        has_won(board, player)
        if has_won(board, player) == True:
            os.system("clear")
            print_board(board, mode)
            print_result(player)
        is_full(board)
        if is_full(board) == True:
            os.system("clear")
            print_board(board, mode)
            print(tie())

        if player == colored("O", 'red'):
            i = colored("X", 'blue')
        elif player == colored("X", 'blue'):
            i = colored("O", 'red')



def empty_cells(board1):

    cells = []

    for x, row in enumerate(board1):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells

def evaluate(board1):

    if wins(board1, COMP):
        score = +1
    elif wins(board1, HUMAN):
        score = -1
    else:
        score = 0

    return score

def wins(board1, player):

    win_state = [
        [board1[0][0], board1[0][1], board1[0][2]],
        [board1[1][0], board1[1][1], board1[1][2]],
        [board1[2][0], board1[2][1], board1[2][2]],
        [board1[0][0], board1[1][0], board1[2][0]],
        [board1[0][1], board1[1][1], board1[2][1]],
        [board1[0][2], board1[1][2], board1[2][2]],
        [board1[0][0], board1[1][1], board1[2][2]],
        [board1[2][0], board1[1][1], board1[0][2]],
    ]
    if [player, player, player] in win_state:
        return True
    else:
        return False

def game_over(board1):

    return wins(board1, HUMAN) or wins(board1, COMP)

def mark_ai(player, row, col,h, c):

    i = 0
    if player == h:
        i = -1
    elif player == c:
        i = +1
    new_board = copy.copy(board1)
    new_board[row][col] = i

    return row,col

def minimax(board1, depth, player,c, h, board):



    if player == COMP:
        best = [-1, -1, -infinity]

    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(board1):
        score = evaluate(board1)

        return [-1, -1, score]

    for cell in empty_cells(board1):
        x, y = cell[0], cell[1]
        board1[x][y] = player
        score = minimax(board1, depth - 1, -player, c, h, board)

        board1[x][y] = 0
        score[0], score[1] = x, y



        if player == COMP:
            if score[2] > best[2]:
                best = score  # max value

        else:
            if score[2] < best[2]:
                best = score  # min value


    return best

def valid_move(x, y):

    if [x, y] in empty_cells(board):
        return True
    else:
        return False

def set_move(x, y, player):

    if valid_move(x, y):
        board[x][y] = player
        return True
    else:
        return False

def ai_turn(board, player, used_letters, c, h,):

    depth = len(empty_cells(board1))
    if depth == 0 or game_over(board1):
        return

    if depth == 9:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
    else:
        move = minimax(board1, depth, COMP, c, h, board)
        row, col = move[0], move[1]

    a = row
    b = col
    if a == 0:
        a = ("A")
    elif a == 1:
        a = ("B")
    elif a == 2:
        a = ("C")
    b += 1
    b = str(b)
    ai_letter = a + b
    used_letters.append(ai_letter)

    return (row, col)




def tictactoe_game5(mode, choose):


    used_letters = []
    board = init_board5()
    for i in range(len(board)):
        for y in range(len(board)):
            if board[i][y] == 0:
                board[i][y] = "."

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    characters = ("X","x","O","o")
    player = str.upper(input("                           please choose and press X or O: "))
    if player == "QUIT":
        print("You quit")
        exit()
    while player not in characters:
        os.system("clear")
        tic_tac_draw()
        draw()
        print("                           Choose a game mode. Press a number from 1 to 8!: ", choose)
        print("""            
                                             invalid character
        """)
        player = str.upper(input("                           please choose and press X or O: "))
    if player == "X":
        i = colored(player, 'blue')
    else:
        i = colored(player, 'red')
    while has_won5(board, player) != True and is_full5(board) != True:
        os.system("clear")
        player = i
        print_board5(board, mode)
        print("\n used coordinates: ", end=" ")
        for letter in used_letters:

            print(letter + ", ", end=" ")

        row, col = get_move5(board, player,used_letters, mode)
        mark(board, player, row, col)
        has_won5(board, player)
        if has_won5(board, player) == True:
            os.system("clear")
            print_board5(board, mode)
            print_result(player)
        is_full5(board)
        if is_full5(board) == True:
            os.system("clear")
            print_board5(board, mode)
            print(tie())

        if player == colored("O", 'red'):
            i = colored("X", 'blue')
        elif player == colored("X", 'blue'):
            i = colored("O", 'red')


def tictactoe_ai5(mode, choose):
    used_letters = []
    board = init_board5()
    for i in range(len(board)):
        for y in range(len(board)):
            if board[i][y] == 0:
                board[i][y] = "."

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    characters = ("X", "x", "O", "o")
    player = str.upper(input("                           please choose and press X or O: "))
    if player == "QUIT":
        print("You quit")
        exit()
    while player not in characters:
        os.system("clear")
        tic_tac_draw()
        draw()
        print("                           Choose a game mode. Press a number from 1 to 8!: ", choose)
        print("""            
                                             invalid character
        """)
        player = str.upper(input("                           please choose and press X or O: "))
    if player == "X":
        i = colored(player, 'blue')
    else:
        i = colored(player, 'red')
    while has_won5(board, player) != True and is_full5(board) != True:
        os.system("clear")
        print_board5(board, mode)
        print("\n used characters: ", end=" ")
        for letter in used_letters:

            print(letter + ", ", end=" ")
        player = i
        row, col = get_move5(board, player,used_letters, mode)
        mark(board, player, row, col)
        if has_won5(board, player) == True:
            os.system("clear")
            print_board5(board, mode)
            print_result(player)
        is_full5(board)
        if is_full5(board) == True:
            os.system("clear")
            print_board5(board, mode)
            print(tie())
        print_board5(board, mode)
        if player == colored("O", 'red'):
            i = colored("X", 'blue')
        elif player == colored("X", 'blue'):
            i = colored("O", 'red')
        player = i
        row, col = get_ai_move5(board, player, used_letters)
        mark(board, player, row, col)
        has_won5(board, player)
        if has_won5(board, player) == True:
            os.system("clear")
            print_board5(board, mode)
            print_result(player)
        is_full5(board)
        if is_full5(board) == True:
            os.system("clear")
            print_board5(board, mode)
            print(tie())

        if player == colored("O", 'red'):
            i = colored("X", 'blue')
        elif player == colored("X", 'blue'):
            i = colored("O", 'red')

def ai_ai5(mode):
    used_letters = []
    board = init_board5()
    for i in range(len(board)):
        for y in range(len(board)):
            if board[i][y] == 0:
                board[i][y] = "."

    player = ("X")

    h = colored(player, 'blue')
    c = colored("O", 'red')
    while has_won5(board, player) != True and is_full5(board) != True:
        os.system("clear")
        player = h
        print_board5(board, mode)
        print("Your turn: ", player)
        time.sleep(1)
        row, col = get_ai_move5(board, player, used_letters)

        mark(board, player, row, col)
        if has_won5(board, player) == True:
            os.system("clear")
            print_board5(board, mode)
            print_result(player)
        is_full5(board)
        if is_full5(board) == True:
            os.system("clear")
            print_board5(board, mode)
            print(tie())

        player = c
        if player == colored("O", 'red'):
            os.system("clear")
            print_board5(board, mode)
            print("Your turn: ", player)
            time.sleep(1)
            row, col = get_ai_move5(board, player, used_letters)
            mark(board, player, row, col)
            has_won5(board, player)
        if has_won5(board, player) == True:
            os.system("clear")
            print_board5(board, mode)
            print_result(player)
        is_full(board)
        if is_full5(board) == True:
            os.system("clear")
            print_board5(board, mode)
            print(tie())

def draw():
    print("                                             1-Human vs Human")
    print("                                             2-Human vs Ai-easy")
    print("                                             3-Human vs Ai-medium")
    print("                                             4-Human vs Ai-hard")
    print("                                             5-Ai vs Ai")
    print("                                             6-Human vs Human  5x5")
    print("                                             7-Human vs Ai-easy 5x5")
    print("""                                             8-Ai vs Ai 5x5"
          """)


def main_menu():
    os.system("clear")

    choose_options = ("1", "2", "3", "4", "5", "6", "7", "8")
    tic_tac_draw()
    draw()

    choose = input("                           Choose a game mode. Press a number from 1 to 8!:  ")
    if choose == "quit" or choose == "QUIT":
        print("You quit")
        exit()

    while choose not in choose_options:
        os.system("clear")
        tic_tac_draw()
        draw()
        print("""                                             invalid characters.
        """)
        choose = input("                           Choose a game mode. Press a number from 1 to 8!:  ")
        if choose == "quit" or choose == "QUIT":
            print("You quit")
            exit()
    if choose == "1":
        tictactoe_game("  Human vs Human", choose)
    elif choose == "2":
        tictactoe_ai(" Human vs Ai-easy", choose)
    elif choose == "3":
        tictactoe_ai_medium("Human vs Ai-medium", choose)
    elif choose == "5":
        ai_ai("     Ai vs Ai")
    elif choose == "4":
        ai_hard(" Human vs Ai-hard", choose)
    elif choose == "6":
        tictactoe_game5("     Human vs Human  5x5", choose)
    elif choose == "7":
        tictactoe_ai5("     Human vs Ai-easy 5x5",choose)
    elif choose == "8":
        ai_ai5("         Ai vs Ai 5x5")

if __name__ == '__main__':
    main_menu()

