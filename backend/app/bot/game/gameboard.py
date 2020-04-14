from typing import Union

import numpy as np
import pandas as pd


class Gameboard:
    def __init__(
        self,
        board_id: int,
        n_rows: int = 3,
        n_cols: int = 3,
        win_score: int = 3,
        board_type: str = "string",
    ) -> None:
        """
        Args:
            ``n_rows`` (`int`): rows to initialize gameboard
            ``n_cols`` (`int`): columns to initialize gameboard
            ``win_score`` (`int`): score needed to win
        """
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.board = np.zeros((self.n_rows, self.n_cols))
        self.win_score = win_score
        self.board_id = board_id
        self.symbols = {0: " ", 1: "X", -1: "O"}
        self.symbols_rev = {" ": 0, "X": 1, "O": -1}
        self.winner = None
        self.draw = None
        self.hash = None

    def str_rep(self) -> None:
        """
        string representation of array, with symbols
        """
        for i in range(self.n_rows):
            row = "|"
            header = "|"
            for j in range(self.n_cols):
                header += "---|"
                row += f" {self.symbols[self.board[i, j]]} |"
            print(header)
            print(row)
        print(header)

    def get_hash(self) -> str:
        """
        basically, return flattened view of board
        """
        self.hash = str(self.board.flatten())
        return self.hash

    def update_board(self, row: int, col: int, sym: Union[int, str]) -> None:
        """
        update array with int representation of symbol if position is valid.

        Args:
            ``row`` (`int`): row to update
            ``col`` (`int`): column to update
            ``sym`` (`int` or `str`): symbol to update row, col with

        """
        if not isinstance(sym, int):
            sym = self.symbols_rev[sym]

        if self.board[row, col] == 0:
            self.board[row, col] = sym
        else:
            print("move not valid, space not empty")

    def check_win(self) -> bool:
        """
        check diagonals, rows, and columns for win_score (+ or -) or draw.

        # TODO: add check to make sure if win_score < n_rows or n_cols,
                that values are next to each other

        Returns:
            `bool`: True if a player won, False if no win or a draw
        """
        left_diag_score = np.sum(np.diag(self.board))
        right_diag_score = np.sum(np.diag(np.fliplr(self.board)))

        row_sums = np.sum(self.board, axis=1)
        col_sums = np.sum(self.board, axis=0)

        x_win = self.win_score
        o_win = self.win_score * -1

        # check if x wins
        if (
            x_win in row_sums
            or x_win in col_sums
            or x_win in [left_diag_score, right_diag_score]
        ):
            self.winner = 1
            # print("game over, X wins")

            return True

        # check if o wins
        if (
            o_win in row_sums
            or o_win in col_sums
            or o_win in [left_diag_score, right_diag_score]
        ):
            self.winner = -1
            # print("game over, O wins")
            return True

        # check if draw
        if 0 not in self.board:
            self.draw = True
            self.winner = 0
            # print("game over, draw")
            return False

        return False

    def reset(self) -> None:
        """
        back to square one
        """
        self.board = np.zeros((self.n_rows, self.n_cols))
        self.winner = None
        self.draw = None
        self.hash = None
