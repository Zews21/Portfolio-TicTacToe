
import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_player = "X"
running = True
winner = None


def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("---------")


def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"


def check_horizontal():
    global winner
    if board[0] == board[1] == board[2] != "-":
        winner = board[0]
        return True

    elif board[3] == board[4] == board[5] != "-":
        winner = board[3]
        return True

    elif board[6] == board[7] == board[8] != "-":
        winner = board[6]
        return True


def check_vertical():
    global winner

    if board[0] == board[3] == board[6] != "-":
        winner = board[0]
        return True

    elif board[1] == board[4] == board[7] != "-":
        winner = board[1]
        return True

    elif board[2] == board[5] == board[8] != "-":
        winner = board[2]
        return True


def check_diagonal():
    global winner
    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
        return True

    elif board[2] == board[4] == board[6] != "-":
        winner = board[2]
        return True


def check_win():
    global running
    if check_horizontal() or check_vertical() or check_diagonal():
        print_board(board)
        print(f"The winner is: {winner}")
        running = False


def check_tie():
    global running
    if "-" not in board:
        print_board(board)
        print("It is a tie!")
        running = False


def computer(board):
    while current_player == "O":
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switch_player()


def player_input():
    player_input = int(input("Pick a number from 1-9: "))
    if 1 <= player_input <= 9 and board[player_input - 1] == "-":
        board[player_input - 1] = current_player
    else:
        print("Invalid move")


while running:
    print_board(board)
    player_input()
    check_win()
    check_tie()
    switch_player()
    computer(board)
    check_win()
    check_tie()
