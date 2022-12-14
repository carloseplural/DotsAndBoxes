import random

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
        self.condition_count = 0
        self.square_above = False
        self.square_below = False
        self.square_right = False
        self.square_left = False

    "Creates the board based on a given input size"
    def create_board(self, size_selection):
        self.size_selection = size_selection
        selection_x = self.size_selection[0]
        selection_y = self.size_selection[1]
        board = self.board

        "Populates the rows"
        for r in range(selection_x):
            board.append(['+', ' '] * (selection_y - 1) + ['+'])
            if r < selection_x - 1:
                board.append([' '] * ((selection_y * 2) - 1))

        "Creates column index"
        columns = self.columns
        for col in range(selection_y):
            columns.append(col)
            if col < (selection_y - 1) and col < 10:
                columns.append(' ')
            elif (selection_y - 1) > col >= 10:
                columns.append('')

        "Creates row index"
        rows = self.rows
        for row in range(selection_x):
            rows.append(row)
            if row < (selection_x - 1):
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
        self.create_board(size_selection=(4, 4))
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
        elif not self.cells_are_adjacent(cell_1, cell_2):
            print("Cells must be adjacent. ", end="")
            return False
        elif not self.cells_are_empty(cell_1, cell_2):
            print("This move has already been played. ", end="")
            return False
        else:
            return True

    "Check if a box can be filled"
    def check_box(self, cell_1, cell_2):
        board = self.board
        self.condition_count = 0

        "Format cell 1"
        cell_1_point_1 = cell_1[0] * 2
        cell_1_point_2 = cell_1[1] * 2

        "Format cell 2"
        cell_2_point_1 = cell_2[0] * 2
        cell_2_point_2 = cell_2[1] * 2

        "If last played line is horizontal, check square above and square below"
        if cell_1_point_1 == cell_2_point_1:
            played_line = (cell_1_point_1, (max(cell_1_point_2, cell_2_point_2) - 1))

            "Check square above"
            try:
                if (
                        board[played_line[0] - 1][played_line[1] - 1] == self.v_line and
                        board[played_line[0] - 2][played_line[1]] == self.h_line and
                        board[played_line[0] - 1][played_line[1] + 1] == self.v_line
                ):
                    self.square_above = True
                    self.condition_count += 1
                else:
                    self.square_above = False
            except IndexError:
                self.square_above = False
                pass
            "check square below"
            try:
                if (
                        board[played_line[0] + 1][played_line[1] + 1] == self.v_line and
                        board[played_line[0] + 2][played_line[1]] == self.h_line and
                        board[played_line[0] + 1][played_line[1] - 1] == self.v_line
                ):
                    self.square_below = True
                    self.condition_count += 1
                else:
                    self.square_below = False
            except IndexError:
                self.square_below = False
                pass

        "If last played line is vertical, check right and left squares"
        if cell_1_point_2 == cell_2_point_2:
            played_line = (max(cell_1_point_1, cell_2_point_1) - 1, cell_1_point_2)

            "Check square right"
            try:
                if (
                        board[played_line[0] + 1][played_line[1] + 1] == self.h_line and
                        board[played_line[0]][played_line[1] + 2] == self.v_line and
                        board[played_line[0] - 1][played_line[1] + 1] == self.h_line
                ):
                    self.square_right = True
                    self.condition_count += 1
                else:
                    self.square_right = False
            except IndexError:
                self.square_right = False
                pass
            "check square left"
            try:
                if (
                        board[played_line[0] - 1][played_line[1] - 1] == self.h_line and
                        board[played_line[0]][played_line[1] - 2] == self.v_line and
                        board[played_line[0] + 1][played_line[1] - 1] == self.h_line
                ):
                    self.square_left = True
                    self.condition_count += 1
                else:
                    self.square_left = False
            except IndexError:
                self.square_left = False
                pass
        if self.condition_count > 0:
            return True
        else:
            return False

    "Fills the box"
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

            "Check above"
            if self.square_above:

                "Fills box"
                board[played_line[0] - 1][played_line[1]] = player

                'Adds a point'
                if player == "A":
                    self.score_player_A += 1
                if player == "B":
                    self.score_player_B += 1
            pass

            "Check below"
            if self.square_below:

                "Fills box"
                board[played_line[0] + 1][played_line[1]] = player

                "Adds a point"
                if player == "A":
                    self.score_player_A += 1
                if player == "B":
                    self.score_player_B += 1
            pass

        "If last played line is vertical, check above and below squares"
        if cell_1_point_2 == cell_2_point_2:
            played_line = (max(cell_1_point_1, cell_2_point_1) - 1, cell_1_point_2)

            "Check right"
            if self.square_right:

                "Fills box"
                board[played_line[0]][played_line[1] + 1] = player

                "Adds a point"
                if player == "A":
                    self.score_player_A += 1
                if player == "B":
                    self.score_player_B += 1
            pass

            "Check left"
            if self.square_left:

                "Fills box"
                board[played_line[0]][played_line[1] - 1] = player

                "Adds a point"
                if player == "A":
                    self.score_player_A += 1
                if player == "B":
                    self.score_player_B += 1
            pass


    "Counts the number of plays"
    def count_play(self):
        self.play_count += 1
        return self.play_count

    "Game ends when the board is full"
    def board_is_full(self):
        play_count = self.play_count
        selection_x = self.size_selection[0]
        selection_y = self.size_selection[1]

        "If x,y is the board size, the board will be full after (2xy - x - y) plays"
        if play_count == (2 * (selection_x * selection_y) - selection_x - selection_y):
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
    def __init__(self, player, gameboard):
        "Initialises symbols"
        self.player = player
        self.play = "o"
        self.h_line = "—"
        self.v_line = "|"
        self.line_played = None

        "Links board"
        self.gameboard = gameboard

        "Board size"
        self.board_x = (len(self.gameboard.board) + 1) // 2
        self.board_y = (len(self.gameboard.board[0]) + 1) // 2


"Player Class"
class Human(Player):

    "Moves the selected player"
    def move_player(self, cell_1, cell_2):
        "Formats cell 1"
        cell_1_point_1 = cell_1[0] * 2
        cell_1_point_2 = cell_1[1] * 2

        "Formats cell 2"
        cell_2_point_1 = cell_2[0] * 2
        cell_2_point_2 = cell_2[1] * 2

        "Creates variable board"
        board = self.gameboard.board

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

"Computer Class"
class Computer(Player):

    "Initialises methods"
    def __init__(self, player, gameboard):
        super().__init__(player, gameboard)
        self.fill_box = None


"Class random computer"
class Random_Computer(Computer):

    "Computer selects and makes the move"
    def move_computer(self):
        board_class = self.gameboard
        board = self.gameboard.board
        board_x = self.board_x
        board_y = self.board_y
        possible_moves = []
        allowed_moves = []

        "Creates list of all possible moves in the board"
        for x in range(board_x):
            for y in range(board_y):
                possible_moves.append((x, y))

        "Creates list of all allowed moves left in the board"
        for p1 in possible_moves:
            for p2 in possible_moves:
                if (board_class.cells_are_empty(cell_1=p1, cell_2=p2) and
                        board_class.cells_are_adjacent(cell_1=p1, cell_2=p2) and
                        p1 != p2
                ):
                    if (p2, p1) not in allowed_moves:
                        allowed_moves.append((p1, p2))
                    pass
                pass

        random_play = random.choice(allowed_moves)
        cell_1 = random_play[0]
        cell_2 = random_play[1]

        "Formats cell 1"
        cell_1_point_1 = cell_1[0] * 2
        cell_1_point_2 = cell_1[1] * 2

        "Formats cell 2"
        cell_2_point_1 = cell_2[0] * 2
        cell_2_point_2 = cell_2[1] * 2

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

        "Check if move draws a box"
        if board_class.check_box(cell_1=cell_1, cell_2=cell_2):
            board_class.fill_box(player="B", cell_1=cell_1, cell_2=cell_2)
            self.fill_box = True
        else:
            self.fill_box = False

"Class smart computer"
class Smart_Computer(Computer):

    "Computer selects and makes the move"
    def move_computer(self):
        board_class = self.gameboard
        board = self.gameboard.board
        board_x = self.board_x
        board_y = self.board_y
        possible_moves = []
        allowed_moves = []
        best_moves = []

        "Creates list of all possible moves in the board"
        for x in range(board_x):
            for y in range(board_y):
                possible_moves.append((x, y))

        "Creates list of all allowed moves left in the board"
        for p1 in possible_moves:
            for p2 in possible_moves:
                if (board_class.cells_are_empty(cell_1=p1, cell_2=p2) and
                        board_class.cells_are_adjacent(cell_1=p1, cell_2=p2) and
                        p1 != p2
                ):
                    if (p2, p1) not in allowed_moves:
                        allowed_moves.append((p1, p2))
                    pass
                pass

        "Creates a sorted list of moves by potential points"
        for a in allowed_moves:
            board_class.check_box(cell_1=a[0], cell_2=a[1])
            if board_class.condition_count == 2:
                best_moves.append(a)
            pass

        for a in allowed_moves:
            board_class.check_box(cell_1=a[0], cell_2=a[1])
            if board_class.condition_count == 1:
                best_moves.append(a)
            pass

        "Select move"
        try:
            cell_1 = best_moves[0][0]
            cell_2 = best_moves[0][1]
        except IndexError:
            random_play = random.choice(allowed_moves)
            cell_1 = random_play[0]
            cell_2 = random_play[1]

        "Formats cell 1"
        cell_1_point_1 = cell_1[0] * 2
        cell_1_point_2 = cell_1[1] * 2

        "Formats cell 2"
        cell_2_point_1 = cell_2[0] * 2
        cell_2_point_2 = cell_2[1] * 2

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

        "Check if move draws a box"
        if board_class.check_box(cell_1=cell_1, cell_2=cell_2):
            board_class.fill_box(player="B", cell_1=cell_1, cell_2=cell_2)
            self.fill_box = True
        else:
            self.fill_box = False


#
#
#
#
#
# zoard = Board()
# zoard.create_board(size_selection=(4,4))
# zoard.check_box(cell_1=(0,0), cell_2=(0,1))
# print(zoard.condition_count)
# Computer("A",zoard).move_computer()
#


