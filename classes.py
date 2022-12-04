# Board class

class Board:

    "Initialises the board as an empty array"
    def __init__(self):
        self.board = []
        self.columns = ['# ']
        self.rows = []

    "Creates the board based on a given input size"
    def create_board(self, size_selection, custom=0):
        "Dictionary that determines the size of the board"
        board_sizes = {
            'small': 4,
            'medium': 10,
            'large': 15,
            'custom': custom
        }

        "Creates cells in the board"
        board = self.board
        selection = board_sizes[size_selection]
        for r in range(selection):
            board.append(['+', ' '] * (selection - 1) + ['+'])
            board.append([' '] * 7)

        "Creates column index"
        columns = self.columns
        for col in range(selection):
            columns.append(col)
            if col < (selection - 1) and col < 10:
                columns.append(' ')
            elif (selection - 1) > col >= 10:
                columns.append('')

        "Creates row index"
        rows = self.rows
        for row in range(selection):
            rows.append(row)
            if row < (selection - 1):
                rows.append(' ')

    "Displays the board"
    def display_board(self):
        board = self.board
        rows = self.rows
        columns = self.columns

        "Creates copy to be displayed as to not change original board"
        board_copy = board.copy()

        "Creates indexes with correct spacing to each row"
        for row in range(len(rows)):
            board_copy[row] = [rows[row]] + ([''] * (2 - len(str(rows[row])))) + board_copy[row]

        "Adds columns indexes with correct spacing"
        for col in columns:
            print(col, end=' ')
        print()

        "Adds row/cells to the board"
        for row in board_copy:
            for col in row:
                print(col, end=' ')
            print()

    "Displays example on a 4x4 board"
    def example(self):
        self.create_board("small")
        example = self.board.copy()
        print("-" * 16)
        example[0][2] = "o"
        example[0][4] = "o"
        example[0][3] = "—"
        self.display_board()
        print("-" * 16)

    "Cell not empty rule"
    def is_cell_empty(self, cell):

        "If the cell has a 'o' instead of '+', it cannot be played"
        if self.board[cell[0] * 2][cell[1] * 2] != "+":
            print("Not valid. Cell is not empty.")
            return False
        "Return true if is empty"
        return True

    "Fill box"

    "Point counter"

    "Reset game"

    "End game"

"Player class"
class Player:

    "---"
    def __init__(self):
        pass

    "Moves the selected player"
    def move_player(self, player, cell_1, cell_2, board):
        "logs the move"
        board.board[cell_1[0] * 2][cell_1[1] * 2] = "o"
        board.board[cell_2[0] * 2][cell_2[1] * 2] = "o"

        "can only move if points are horizontally or diagonally adjacent"
        if cell_1[0] != cell_2[0] and cell_1[1] != cell_2[1]:
            print("Not valid. Cells must be adjacent")
            return False
        elif (int(cell_1[0]) - int(cell_2[0])) not in range(-1, 2) or (int(cell_1[1]) - int(cell_2[1])) not in range(-1, 2):
            print("Not valid. Cells must be adjacent")
            return False
        else:
            return True

    # Player vs computer

