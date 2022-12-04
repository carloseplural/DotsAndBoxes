# Importing classes from the classes.py file
from classes import Board
from classes import Player
import ast
import random

"Input desired board size"
range_list = ["small", "medium", "large", "custom"] + [str(r) for r in range(3, 26)]
size_selection = input("Enter board size \nSmall (4x4), Medium (9x9), Large (15x15) or Custom (x by x, min=3, max=25): ")

"Input must be a valid range"
while size_selection not in range_list:
    print("Not valid")
    size_selection = input("Enter board size \nmall (4x4), Medium (9x9), Large (15x15) or Custom (x by x, min=3, max=25): ").lower()

"Select custom size if option is chosen"
if size_selection not in ["small", "medium", "large"]:
    if size_selection == "custom":
        custom = int(input("Choose size x (x by x): "))
        while custom not in list(range(3, 26)):
            print("Not valid")
            custom = int(input("Choose size x (x by x): "))
    else:
        custom = int(size_selection)
        size_selection = "custom"
else:
    custom = 0

"Show game example"
print("\nChoose two cardinal points to make a move (x1, y1) (x2, y2)", "Example: (0,1) (0,2)", sep="\n")
example = Board()
example.example()

"Creates player list"
player_A = "A"
player_B = "B"
player_list = [player_A, player_B]
p1 = Player()
p2 = Player()

"Run the game"
while True:
    "Generates the game board"
    board = Board()
    board.create_board(size_selection="small", custom="custom")
    board.display_board()

    "Randomizes first move"
    random.shuffle(player_list)
    player_1 = player_list[0]
    player_2 = player_list[1]
    print(f"Player {player_1} moves first!")

    # while True:
    #     "Logs move for each player in tuples"
    #     try:
    #         cell_1 = ast.literal_eval(input("Enter first point 'x1, y1': "))
    #         while not board.is_cell_empty(cell=cell_1):
    #             cell_1 = ast.literal_eval(input("Enter first point 'x1, y1': "))
    # break








