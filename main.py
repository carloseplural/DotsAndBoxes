from classes import Board

while True:
    # Input desired board size
    size_selection = input("Enter board size \nsmall (4x4), medium (9x9), large (15x15) or custom): ").lower()
    # If input is invalid, enter again
    while size_selection not in ["small", "medium", "large", "custom"]:
        print("Not valid")
        size_selection = input("Enter board size \nsmall (4x4), medium (9x9), large (15x15) or custom): ").lower()

    # Generates the game board
    board = Board()
    board.create_board(size_selection)
    board.display_board()
    break
