import pandas as pd

class Board():
    """initialises the board as an empty array"""
    def __init__(self):
        self.board = []

      """creates the board based on a given input"""
    def create_board(self, size_selection):
        board_sizes = {
            "small": 4,
            "medium": 10,
            "large": 15
        }
        if size_selection == "custom":
            custom = int(input("Choose a size x (x by x): "))
            board_sizes["custom"] = custom
        for r in range(board_sizes[size_selection]):
            self.board.append(r + 1)
            self.board.append("")
        self.board = pd.DataFrame(data="", columns=self.board, index=self.board)
        for row in range(1, board_sizes[size_selection] + 1):
            for col in range(1, board_sizes[size_selection] + 1):
                self.board.loc[row, col] = "+"

    def display_board(self):
        """"""
        print(self.board)

    def