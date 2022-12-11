# Importing classes from the classes.py file
from classes import Board, Player
import ast
import random

"Show game example"
example = Board()
example.example()

"Input board size"
while True:
    try:
        size_selection = int(input("Enter board size x as integer (min 3, max 15): "))
        break
    except ValueError:
        print("Not valid. ", end="")
        continue

while size_selection < 3:
    size_selection = int(input("Minimum board size is 3. Enter board size x as integer (min 3, max 15): "))

while size_selection > 15:
    size_selection = int(input("Maximum board size is 15. Enter board size x as integer (min 3, max 15): "))

"Starts the game"
while True:

    "Creates player instances"
    player_list = ["A", "B"]
    random.shuffle(player_list)
    letter_1 = player_list[0]
    letter_2 = player_list[1]
    player_1 = Player(player=letter_1)
    player_2 = Player(player=letter_2)
    play_count = 0

    "Initialises the board"
    gameboard = Board()
    gameboard.create_board(size_selection=size_selection)

    "Displays the board"
    gameboard.display_board()
    gameboard.get_score()
    print(f"Player {letter_1} plays first!")

    "Run the game"
    while True:

        turn = 0
        "Player 1 moves"
        while turn == 0 and gameboard.board_is_full() == False:

            "Enter cells and checks for errors"
            check_error = 1
            while True:
                while check_error == 1:
                    try:
                        cell_1 = ast.literal_eval(input(f"Player {letter_1}, enter first cell 'x1, y1': "))
                        while cell_1[0] > (size_selection - 1) or cell_1[1] > (size_selection - 1) or cell_1[0] < 0 or cell_1[1] < 0:
                            cell_1 = ast.literal_eval(input(f"Coordinate has to be in range between 0 and {size_selection - 1}. Enter again 'x1, y1': "))
                        check_error = 2
                        break
                    except (ValueError, SyntaxError, TypeError):
                        print("Not valid. ", end="")
                        continue

                while check_error == 2:
                    try:
                        cell_2 = ast.literal_eval(input(f"Player {letter_1}, enter second cell 'x1, y1': "))
                        while cell_2[0] > (size_selection - 1) or cell_2[1] > (size_selection - 1) or cell_2[0] < 0 or cell_2[1] < 0:
                            cell_2 = ast.literal_eval(input(f"Coordinate has to be in range between 0 and {size_selection - 1}. Enter again 'x1, y1': "))
                        check_error = 0
                        break
                    except (ValueError, SyntaxError, TypeError):
                        print("Not valid. ", end="")
                        continue

                "Checks the rules"
                if not gameboard.check_rules(cell_1=cell_1, cell_2=cell_2):
                    check_error = 1
                else:
                    break

            "Logs move and displays board"
            player_1.move_player(gameboard=gameboard, cell_1=cell_1, cell_2=cell_2)
            gameboard.count_play()
            if gameboard.fill_box(player=letter_1, cell_1=cell_1, cell_2=cell_2):
                turn = 0
            else:
                turn = 1
            gameboard.display_board()
            gameboard.get_score()

        "Player 2 moves"
        while turn == 1 and gameboard.board_is_full() == False:

            "Enter cells and checks for errors"
            check_error = 1
            while True:
                while check_error == 1:
                    try:
                        cell_1 = ast.literal_eval(input(f"Player {letter_2}, enter first cell 'x1, y1': "))
                        while cell_1[0] > (size_selection - 1) or cell_1[1] > (size_selection - 1) or cell_1[0] < 0 or cell_1[1] < 0:
                            cell_1 = ast.literal_eval(input(f"Coordinate has to be in range between 0 and {size_selection - 1}. Enter again 'x1, y1': "))
                        check_error = 2
                        break
                    except (ValueError, SyntaxError, TypeError):
                        print("Not valid. ", end="")
                        continue

                while check_error == 2:
                    try:
                        cell_2 = ast.literal_eval(input(f"Player {letter_2}, enter second cell 'x1, y1': "))
                        while cell_2[0] > (size_selection - 1) or cell_2[1] > (size_selection - 1) or cell_2[0] < 0 or cell_2[1] < 0:
                            cell_2 = ast.literal_eval(input(f"Coordinate has to be in range between 0 and {size_selection - 1}. Enter again 'x1, y1': "))
                        check_error = 0
                        break
                    except (ValueError, SyntaxError, TypeError):
                        print("Not valid. ", end="")
                        continue

                "Checks the rules"
                if not gameboard.check_rules(cell_1=cell_1, cell_2=cell_2):
                    check_error = 1
                else:
                    break

            "Logs move and displays board"
            player_2.move_player(gameboard=gameboard, cell_1=cell_1, cell_2=cell_2)
            gameboard.count_play()
            if gameboard.fill_box(player=letter_2, cell_1=cell_1, cell_2=cell_2):
                turn = 1
            else:
                turn = 0
            gameboard.display_board()
            gameboard.get_score()

        "Checks if the board is full"
        if gameboard.board_is_full():

            "If yes display the winner ot tie"
            gameboard.get_winner()
            break
        else:
            continue

    "Reset game"
    if gameboard.reset_game():
        continue
    else:
        break
