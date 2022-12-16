# Importing classes from the classes.py file
from classes import Board, Human, Smart_Computer, Random_Computer, Synchronous
import ast
import random

"Game mode"
print("Select game mode: ", "1 - PLayer vs Player", "2 - Player vs PC (easy)", "3 - Player vs PC (less easy)", "4 - Player vs PC (synchronous)", sep="\n")
mode = input("Enter number: ")
while mode not in ['1', '2', '3', '4']:
    mode = input("Not valid. Enter number: ")

"Input board size"
while True:
    try:
        size_selection = ast.literal_eval(input("Enter board size x,y. x = Rows, y = Columns  (min x,y = 3): "))
        while size_selection[0] < 3 or size_selection[1] < 3:
            size_selection = ast.literal_eval(input("Cols and rows must be at least size 3. Enter board size x,y as integer (min x,y = 3): "))
        break
    except (ValueError, SyntaxError, TypeError):
        print("Not valid. ", end="")
        continue

selection_x = size_selection[0]
selection_y = size_selection[1]

"Show game example"
example = Board()
example.example()

"Starts a player vs player game"
while mode == "1":

    "Initialises the board"
    gameboard = Board()
    gameboard.create_board(size_selection=size_selection)

    "Creates player instances"
    player_list = ["A", "B"]
    random.shuffle(player_list)
    letter_1 = player_list[0]
    letter_2 = player_list[1]
    player_1 = Human(gameboard=gameboard, player=letter_1)
    player_2 = Human(gameboard=gameboard, player=letter_2)


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
                        while cell_1[0] > (selection_x - 1) or cell_1[1] > (selection_y - 1) or cell_1[0] < 0 or cell_1[1] < 0:
                            cell_1 = ast.literal_eval(input(f"Coordinate not in range. Enter again 'x1, y1': "))
                        check_error = 2
                        break
                    except (ValueError, SyntaxError, TypeError, IndexError):
                        print("Not valid. ", end="")
                        continue

                while check_error == 2:
                    try:
                        cell_2 = ast.literal_eval(input(f"Player {letter_1}, enter second cell 'x1, y1': "))
                        while cell_2[0] > (selection_x - 1) or cell_2[1] > (selection_y - 1) or cell_2[0] < 0 or cell_2[1] < 0:
                            cell_2 = ast.literal_eval(input(f"Coordinate not in range. Enter again 'x1, y1': "))
                        check_error = 0
                        break
                    except (ValueError, SyntaxError, TypeError, IndexError):
                        print("Not valid. ", end="")
                        continue

                "Checks the rules"
                if not gameboard.check_rules(cell_1=cell_1, cell_2=cell_2):
                    check_error = 1
                else:
                    break

            "Logs move"
            player_1.move_player(cell_1=cell_1, cell_2=cell_2)

            "Adds one play to the total"
            gameboard.count_play()

            "Check if a box has been filled"
            if gameboard.check_box(cell_1=cell_1, cell_2=cell_2):
                gameboard.fill_box(player=letter_1, cell_1=cell_1, cell_2=cell_2)

                "If yes player plays again"
                turn = 0
            else:
                "If not moves to next player"
                turn = 1

            "Display board and score"
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
                        while cell_1[0] > (selection_x - 1) or cell_1[1] > (selection_y - 1) or cell_1[0] < 0 or cell_1[1] < 0:
                            cell_1 = ast.literal_eval(input(f"Coordinate not in range. Enter again 'x1, y1': "))
                        check_error = 2
                        break
                    except (ValueError, SyntaxError, TypeError, IndexError):
                        print("Not valid. ", end="")
                        continue

                while check_error == 2:
                    try:
                        cell_2 = ast.literal_eval(input(f"Player {letter_2}, enter second cell 'x1, y1': "))
                        while cell_2[0] > (selection_x - 1) or cell_2[1] > (selection_y - 1) or cell_2[0] < 0 or cell_2[1] < 0:
                            cell_2 = ast.literal_eval(input(f"Coordinate not in range. Enter again 'x1, y1': "))
                        check_error = 0
                        break
                    except (ValueError, SyntaxError, TypeError, IndexError):
                        print("Not valid. ", end="")
                        continue

                "Checks the rules"
                if not gameboard.check_rules(cell_1=cell_1, cell_2=cell_2):
                    check_error = 1
                else:
                    break

            "Logs move"
            player_2.move_player(cell_1=cell_1, cell_2=cell_2)

            "Adds one play to the total"
            gameboard.count_play()

            "Check if a box has been filled"
            if gameboard.check_box(cell_1=cell_1, cell_2=cell_2):
                gameboard.fill_box(player=letter_2, cell_1=cell_1, cell_2=cell_2)

                "If yes player plays again"
                turn = 1
            else:
                "If not moves to next player"
                turn = 0

            "Display board and score"
            gameboard.display_board()
            gameboard.get_score()

        "Checks if the board is full"
        if gameboard.board_is_full():

            "If yes display the winner or tie"
            gameboard.get_winner()
            break
        else:
            continue

    "Reset game"
    if gameboard.reset_game():
        continue
    else:
        break

"Player vs PC (turns) mode"
while mode == "2" or mode == "3":

    "Initialises the board"
    gameboard = Board()
    gameboard.create_board(size_selection=size_selection)

    "Creates player instances"
    player = Human(gameboard=gameboard, player="A")
    if mode == "2":
        computer = Random_Computer(gameboard=gameboard, player="B")
    if mode == "3":
        computer = Smart_Computer(gameboard=gameboard, player="B")

    player_list = [player, computer]
    random.shuffle(player_list)
    player_1 = player_list[0]
    player_2 = player_list[1]

    "Displays the board"
    gameboard.display_board()
    gameboard.get_score()
    if player_1 == player:
        print("You play first! (A)")
    else:
        print("Computer plays first! (B)")

    "Run the game"
    while True:

        turn = 0
        "Player 1 moves"
        while turn == 0 and gameboard.board_is_full() == False:

            "Checks if the first player is human, if yes then will ask to input cell"
            if player_1 == player:

                "Enter cells and checks for errors"
                check_error = 1
                while True:
                    while check_error == 1:
                        try:
                            cell_1 = ast.literal_eval(input(f"Enter first cell 'x1, y1': "))
                            while cell_1[0] > (selection_x - 1) or cell_1[1] > (selection_y - 1) or cell_1[0] < 0 or cell_1[1] < 0:
                                cell_1 = ast.literal_eval(input(f"Coordinate not in range. Enter again 'x1, y1': "))
                            check_error = 2
                            break
                        except (ValueError, SyntaxError, TypeError, IndexError):
                            print("Not valid. ", end="")
                            continue

                    while check_error == 2:
                        try:
                            cell_2 = ast.literal_eval(input(f"Enter second cell 'x1, y1': "))
                            while cell_2[0] > (selection_x - 1) or cell_2[1] > (selection_y - 1) or cell_2[0] < 0 or cell_2[1] < 0:
                                cell_2 = ast.literal_eval(input(f"Coordinate not in range. Enter again 'x1, y1': "))
                            check_error = 0
                            break
                        except (ValueError, SyntaxError, TypeError, IndexError):
                            print("Not valid. ", end="")
                            continue

                    "Checks the rules"
                    if not gameboard.check_rules(cell_1=cell_1, cell_2=cell_2):
                        check_error = 1
                    else:
                        break

                "Logs move"
                player.move_player(cell_1=cell_1, cell_2=cell_2)

                "Adds one play to the total"
                gameboard.count_play()

                "Check if a box has been filled"
                if gameboard.check_box(cell_1=cell_1, cell_2=cell_2):
                    gameboard.fill_box(player="A", cell_1=cell_1, cell_2=cell_2)

                    "If yes player plays again"
                    turn = 0
                else:
                    "If not moves to next player"
                    turn = 1

            "If player is the computer, input cell automatically"
            if player_1 == computer:
                computer.move_computer()
                gameboard.count_play()

                "If box is filled, computer plays again"
                if computer.fill_box:
                    turn = 0
                else:
                    turn = 1

            "Display board and score"
            gameboard.display_board()
            gameboard.get_score()

        "Player 2 moves"
        while turn == 1 and gameboard.board_is_full() == False:

            "Checks if the second player is human, if yes then will ask to input cell"
            if player_2 == player:

                "Enter cells and checks for errors"
                check_error = 1
                while True:
                    while check_error == 1:
                        try:
                            cell_1 = ast.literal_eval(input(f"Enter first cell 'x1, y1': "))
                            while cell_1[0] > (selection_x - 1) or cell_1[1] > (selection_y - 1) or cell_1[0] < 0 or cell_1[1] < 0:
                                cell_1 = ast.literal_eval(input(f"Coordinate not in range. Enter again 'x1, y1': "))
                            check_error = 2
                            break
                        except (ValueError, SyntaxError, TypeError, IndexError):
                            print("Not valid. ", end="")
                            continue

                    while check_error == 2:
                        try:
                            cell_2 = ast.literal_eval(input(f"Enter second cell 'x1, y1': "))
                            while cell_2[0] > (selection_x - 1) or cell_2[1] > (selection_y - 1) or cell_2[0] < 0 or cell_2[1] < 0:
                                cell_2 = ast.literal_eval(input(f"Coordinate not in range. Enter again 'x1, y1': "))
                            check_error = 0
                            break
                        except (ValueError, SyntaxError, TypeError, IndexError):
                            print("Not valid. ", end="")
                            continue

                    "Checks the rules"
                    if not gameboard.check_rules(cell_1=cell_1, cell_2=cell_2):
                        check_error = 1
                    else:
                        break

                "Logs move"
                player.move_player(cell_1=cell_1, cell_2=cell_2)

                "Adds one play to the total"
                gameboard.count_play()

                "Check if a box has been filled"
                if gameboard.check_box(cell_1=cell_1, cell_2=cell_2):
                    gameboard.fill_box(player="A", cell_1=cell_1, cell_2=cell_2)

                    "If yes player plays again"
                    turn = 1
                else:
                    "If not moves to next player"
                    turn = 0

            "If player is the computer, input cell automatically"
            if player_2 == computer:
                computer.move_computer()
                gameboard.count_play()

                "If box is filled, computer plays again"
                if computer.fill_box:
                    turn = 1
                else:
                    turn = 0

            "Display board and score"
            gameboard.display_board()
            gameboard.get_score()

        "Checks if the board is full"
        if gameboard.board_is_full():
            "If yes display the winner or tie"
            gameboard.get_winner()
            break
        else:
            continue

    "Reset game"
    if gameboard.reset_game():
        continue
    else:
        break

while mode == "4":

    "Initialises the board"
    gameboard = Board()
    gameboard.create_board(size_selection=size_selection)

    "Creates player instances"
    synchronous = Synchronous(gameboard=gameboard)

    "Displays the board"
    gameboard.display_board()
    gameboard.get_score()
    print("Players play simultaneously!")

    "Players moves"
    while True:

        "Enter cells and checks for errors"
        check_error = 1
        while check_error == 1:
            try:
                cell_1 = ast.literal_eval(input(f"Enter first cell 'x1, y1': "))
                while cell_1[0] > (selection_x - 1) or cell_1[1] > (selection_y - 1) or cell_1[0] < 0 or cell_1[1] < 0:
                    cell_1 = ast.literal_eval(input(f"Coordinate not in range. Enter again 'x1, y1': "))
                check_error = 2
                break
            except (ValueError, SyntaxError, TypeError, IndexError):
                print("Not valid. ", end="")
                continue

        while check_error == 2:
            try:
                cell_2 = ast.literal_eval(input(f"Enter second cell 'x1, y1': "))
                while cell_2[0] > (selection_x - 1) or cell_2[1] > (selection_y - 1) or cell_2[0] < 0 or cell_2[1] < 0:
                    cell_2 = ast.literal_eval(input(f"Coordinate not in range. Enter again 'x1, y1': "))
                check_error = 0
                break
            except (ValueError, SyntaxError, TypeError, IndexError):
                print("Not valid. ", end="")
                continue

        "Logs move"
        synchronous.move_synchronous(player_cell_1=cell_1, player_cell_2=cell_2)

        "Display board and score"
        print("")
        gameboard.display_board()
        gameboard.get_score()

        "Checks if the board is full"
        if gameboard.board_is_full():
            "If yes display the winner or tie"
            gameboard.get_winner()
            break
        else:
            continue

    "Reset game"
    if gameboard.reset_game():
        continue
    else:
        break
