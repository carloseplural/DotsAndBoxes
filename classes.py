"""Creating board class"""
class Board:

    "Initialises the board variables"
    def __init__(self):

        self.board = []
        self.size_selection = None
        self.columns = ['# ']
        self.rows = []
        self.play = "o"
        self.h_line = "—"
        self.v_line = "|"
        self.score_player_A = 0
        self.score_player_B = 0
        self.play_count = 0

    "Creates the board based on a given input size"
    def create_board(self, size_selection):
        self.size_selection = int(size_selection)
        selection = self.size_selection

        "Populates the board"
        board = self.board

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
        print("\nChoose two cardinal points to make a move (x1, y1) (x2, y2)", "Example: (0,1) (0,2)", sep="\n")
        self.create_board(size_selection=4)
        example = self.board.copy()
        print("-" * 16)
        example[0][2] = "o"
        example[0][4] = "o"
        example[0][3] = "—"
        self.display_board()
        print("-" * 16)

    "Displays score"
    def get_score(self):
        print("-" * 20)
        print(f"Score: A - {self.score_player_A} | B - {self.score_player_B}")
        print("-" * 20)

    "Cells are not empty rule"
    def cells_are_empty(self, cell_1, cell_2):

        "Format cell 1"
        cell_1_point_1 = cell_1[0] * 2
        cell_1_point_2 = cell_1[1] * 2

        "Format cell 2"
        cell_2_point_1 = cell_2[0] * 2
        cell_2_point_2 = cell_2[1] * 2

        "If target cell has a '-' or '|' it cannot be played"
        if cell_1_point_1 == cell_2_point_1:
            if self.board[cell_1_point_1][max(cell_1_point_2, cell_2_point_2) - 1] == self.h_line:
                return False
            return True
        if cell_1_point_2 == cell_2_point_2:
            if self.board[max(cell_1_point_1, cell_2_point_1) - 1][cell_1_point_2] == self.v_line:
                return False
            return True

    "Rule stating that cells must be adjacent"
    def cells_are_adjacent(self, cell_1, cell_2):

        "Format cell 1"
        cell_1_point_1 = cell_1[0] * 2
        cell_1_point_2 = cell_1[1] * 2

        "Format cell 2"
        cell_2_point_1 = cell_2[0] * 2
        cell_2_point_2 = cell_2[1] * 2

        "can only move if cells are horizontally or vertically adjacent"
        if cell_1_point_1 != cell_2_point_1 and cell_1_point_2 != cell_2_point_2:
            return False
        elif (int(cell_1_point_1) - int(cell_2_point_1)) not in range(-2, 3):
            return False
        elif (int(cell_1_point_2) - int(cell_2_point_2)) not in range(-2, 3):
            return False
        else:
            return True

    "Cells must be different"
    def cells_are_different(self, cell_1, cell_2):
        if cell_1 == cell_2:
            return False
        else:
            return True

    "Check all the rules"
    def check_rules(self, cell_1, cell_2):
        if not self.cells_are_different(cell_1, cell_2):
            print("Cells must be different. ", end="")
            return False
        elif not self.cells_are_adjacent(cell_1,cell_2):
            print("Cells must be adjacent. ", end="")
            return False
        elif not self.cells_are_empty(cell_1, cell_2):
            print("This move has already been played. ", end="")
        else:
            return True

    "Fill box if a square is drawn"
    def fill_box(self, player, cell_1, cell_2):
        board = self.board
        "Format cell 1"
        cell_1_point_1 = cell_1[0] * 2
        cell_1_point_2 = cell_1[1] * 2

        "Format cell 2"
        cell_2_point_1 = cell_2[0] * 2
        cell_2_point_2 = cell_2[1] * 2

        "If last played line is horizontal, check square above and square below"
        if cell_1_point_1 == cell_2_point_1:
            played_line = (cell_1_point_1, (max(cell_1_point_2, cell_2_point_2) - 1))
            condition_count = 0
            "Check square above"
            try:
                if (
                        board[played_line[0] - 1][played_line[1] - 1] == self.v_line and
                        board[played_line[0] - 2][played_line[1]] == self.h_line and
                        board[played_line[0] - 1][played_line[1] + 1] == self.v_line
                ):
                    "If they are all filled, draw the player's letter in the middle"
                    board[played_line[0] - 1][played_line[1]] = player
                    condition_count += 1
                    "Adds a point if box is filled"
                    if player == "A":
                        self.score_player_A += 1
                    if player == "B":
                        self.score_player_B += 1
            except IndexError:
                pass
            "check square below"
            try:
                if (
                        board[played_line[0] + 1][played_line[1] + 1] == self.v_line and
                        board[played_line[0] + 2][played_line[1]] == self.h_line and
                        board[played_line[0] + 1][played_line[1] - 1] == self.v_line
                ):
                    board[played_line[0] + 1][played_line[1]] = player
                    condition_count += 1
                    if player == "A":
                        self.score_player_A += 1
                    if player == "B":
                        self.score_player_B += 1
            except IndexError:
                pass
            if condition_count > 0:
                return True

        "If last played line is vertical, check right and left squares"
        if cell_1_point_2 == cell_2_point_2:
            played_line = (max(cell_1_point_1, cell_2_point_1) - 1, cell_1_point_2)
            condition_count = 0
            "check square to the right"
            try:
                if (
                        board[played_line[0] - 1][played_line[1] + 1] == self.h_line and
                        board[played_line[0]][played_line[1] + 2] == self.v_line and
                        board[played_line[0] + 1][played_line[1] + 1] == self.h_line
                ):
                    "If they are all filled, draw the player's letter in the middle"
                    board[played_line[0]][played_line[1] + 1] = player
                    condition_count += 1
                    if player == "A":
                        self.score_player_A += 1
                    if player == "B":
                        self.score_player_B += 1
            except IndexError:
                pass
            "check square to the left"
            try:
                if (
                        board[played_line[0] + 1][played_line[1] - 1] == self.h_line and
                        board[played_line[0]][played_line[1] - 2] == self.v_line and
                        board[played_line[0] - 1][played_line[1] - 1] == self.h_line
                ):
                    board[played_line[0]][played_line[1] - 1] = player
                    condition_count += 1
                    if player == "A":
                        self.score_player_A += 1
                    if player == "B":
                        self.score_player_B += 1
            except IndexError:
                pass
            if condition_count > 0:
                return True

    "Counts the number of plays"
    def count_play(self):
        self.play_count += 1
        return self.play_count

    "Game ends when the board is full"
    def board_is_full(self):
        play_count = self.play_count

        "If x is the board size, the board will be full after 2(x^2 - x) plays"
        if play_count == (((self.size_selection - 1) * self.size_selection) * 2):
            return True
        else:
            return False

    "Returns winner/tie"
    def get_winner(self):
        if self.score_player_A > self.score_player_B:
            print("Player A wins!")
        elif self.score_player_B > self.score_player_A:
            print("Player B wins!")
        else:
            print("It's a tie!")

    "Resets game"
    def reset_game(self):
        reset = input("Play again? (Y/N)").upper()
        while reset not in ['Y', 'N']:
            reset = input("Not valid. Play again? enter 'Y' or 'N')").upper()

        if reset == "Y":
            return True

        if reset == "N":
            return False

"Creating player class"
class Player:

    "Initialises player 1 and player 2"
    def __init__(self, player):

        "Initialises symbols"
        self.player = player
        self.play = "o"
        self.h_line = "—"
        self.v_line = "|"
        self.score = 0
        self.line_played = None

    "Moves the selected player"
    def move_player(self, gameboard, cell_1, cell_2):
        "Cell 1"
        cell_1_point_1 = cell_1[0] * 2
        cell_1_point_2 = cell_1[1] * 2

        "Cell 2"
        cell_2_point_1 = cell_2[0] * 2
        cell_2_point_2 = cell_2[1] * 2

        "Creates variable board"
        board = gameboard.board

        "logs the move"
        board[cell_1_point_1][cell_1_point_2] = self.play
        board[cell_2_point_1][cell_2_point_2] = self.play

        "draws line between cells"
        "if cells are horizontally adjacent draw an horizontal line"
        if cell_1_point_1 == cell_2_point_1:
            board[cell_1_point_1][(max(cell_1_point_2, cell_2_point_2) - 1)] = self.h_line

        "if cells are vertically adjacent draw a vertical line"
        if cell_1_point_2 == cell_2_point_2:
            board[max(cell_1_point_1, cell_2_point_1) - 1][cell_1_point_2] = self.v_line

    "Player vs computer"
