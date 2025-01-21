'''
Title: Tic-Tac-Toe
Author: Kevin H. Truong
'''

# imports
import random
import time
import os
from settings import *

# Clears the screen
def clear_screen():
    os.system('cls')

# Returns a random number between (and including) the two given numbers
def random_number_between(lowestNumber: int, highestNumber: int):
    return random.randrange(lowestNumber,highestNumber + 1)

# Returns True if the board is full, returns False otherwise
def is_board_full(board):
    for i in range(ROW_AMOUNT):
        for j in range(COLUMN_AMOUNT):
            if (board[i][j] == ' '):
                return False
    return True

def print_board(board):
    for i in range(ROW_AMOUNT):
        for j in range(COLUMN_AMOUNT):
            print(f"[{board[i][j]}]", end = "")
        print("")

 # Gets the position a given player wants to place on the grid, allows user to quit
def player_turn(board, playerName, mark):
    validInput: bool = False
    while (validInput == False):
        # Prints the turn number, the board, and which player's turn it is
        print(f"Turn {turnNumber}")
        print_board(board)
        print(f"{playerName}'s turn")

        # Gets a row and column from the current player (exits if user enters '0'
        print("Row Number: ", end="")
        rowNumber: int = int(input())
        if (rowNumber == 0):
            exit()
        print("Column Number: ", end="")
        columnNumber: int = int(input())
        if (columnNumber == 0):
            exit()

        # Validifies and places the mark if the spot is empty and is within the range of the grid
        if ((board[rowNumber - 1][columnNumber - 1] == ' ') and (rowNumber <= ROW_AMOUNT) and (columnNumber <= COLUMN_AMOUNT)):
            validInput = True
            board[rowNumber - 1][columnNumber - 1] = mark;
        else:
            validInput = False

        clear_screen()
# Checks for a winner for the current board, returns the marker of the winner or returns ' ' if there is no winner
def checkWinner(board):
    # Checks for horizontal win
    for rowNum in range(ROW_AMOUNT):
        columnNum: int = 1
        sameMarksInRow: int = 1
        while (columnNum < COLUMN_AMOUNT):
            if (board[rowNum][0] == board[rowNum][columnNum]):
                sameMarksInRow += 1
            columnNum += 1
        if (sameMarksInRow == WIN_CONDITION):
            return board[rowNum][0]

    # Checks for vertical win
    for columnNum in range(COLUMN_AMOUNT):
        rowNum: int = 1
        sameMarksInColumn: int = 1
        while (rowNum < ROW_AMOUNT):
            if (board[0][columnNum] == board[rowNum][columnNum]):
                sameMarksInColumn += 1
            rowNum += 1
        if (sameMarksInColumn == WIN_CONDITION):
            return board[0][columnNum]

    # Checks for diagonal win (top-left to bottom-right)
    rowNum: int = 1
    columnNum: int = 1
    sameMarksInDiagonal: int = 1
    while rowNum < GRID_SIDE_LENGTH and columnNum < GRID_SIDE_LENGTH:
        if board[0][0] == board[rowNum][columnNum]:
            sameMarksInDiagonal += 1
        rowNum += 1
        columnNum += 1
    if sameMarksInDiagonal == GRID_SIDE_LENGTH:
        return board[0][0]
    
    # Checks for diagonal win (bottom-left to top-right)
    rowNum: int = GRID_SIDE_LENGTH - 2
    columnNum: int = 1
    sameMarksInDiagonal:int = 1
    while rowNum >= 0 and columnNum < GRID_SIDE_LENGTH:
        if board[GRID_SIDE_LENGTH - 1][0] == board[rowNum][columnNum]:
            sameMarksInDiagonal += 1
        rowNum -= 1
        columnNum += 1
    if sameMarksInDiagonal == GRID_SIDE_LENGTH:
        return board[GRID_SIDE_LENGTH - 1][0]    
    
    return ' '


# Gets the names of the two players
print("What is the name of the first player?: ", end = "")
firstPlayerName: str = input()
print("What is the name of the second player?: ", end = "")
secondPlayerName:str = input()

# Picks the player who will go first (represented by 'X'), in which
# the other player will go second (represented by 'O')
firstTurn: int =  random_number_between(1, 2)
if (firstTurn == 1):
    print(f"{firstPlayerName} will go first, and will be represented by X.")
    playerEx: str = firstPlayerName
    print(f"{secondPlayerName} will go second, and will be represented by O.")
    playerOh: str = secondPlayerName
elif (firstTurn == 2):
    print(f"{secondPlayerName} will go first, and will be represented by X.")
    playerEx: str = secondPlayerName
    print(f"{firstPlayerName} will go second, and will be represented by O.")
    playerOh: str = firstPlayerName

time.sleep(5)
clear_screen()

print(f"Row numbers will be between 1 and {ROW_AMOUNT}.")
print(f"Column numbers will be between 1 and {COLUMN_AMOUNT}.")
print("Type '0' anytime to quit.")

time.sleep(3.5)
clear_screen()

# Sets up the game and the initial, empty board
board: chr = []

for _ in range(ROW_AMOUNT):
    board.append([])
    for _ in range(COLUMN_AMOUNT):
        board[-1].append(' ')
winner: chr = ' '

# Loops until a player wins or the board is full (draw)
while ((is_board_full(board) == False) and (winner == ' ')):
    # X's turn
    if (turnNumber % 2 == 1):
        player_turn(board, playerEx, 'X')
    # O's turn
    elif (turnNumber % 2 == 0):
        player_turn(board, playerOh, 'O')

    winner = checkWinner(board)
    clear_screen()
    turnNumber += 1

# Prints the board at the end of the game and prints the winner (or states if it is a draw)
print(f"Turn {turnNumber}")
print_board(board)
print("")
print("Winner: ", end = "")
if (winner == 'X'):
    print(playerEx)
elif (winner == 'O'):
    print(playerOh)
else:
    print("Draw")