import numpy as np
import pandas as pd

from .gameboard import Gameboard


class Player:
    def __init__(self, symbol: int) -> None:
        self.symbol = symbol

    def make_move(
        self, row: int, col: int, board: Gameboard, board_type: str = "string"
    ) -> bool:
        board.update_board(row, col, self.symbol)

        if board_type == "string":
            board.str_rep()
        win = board.check_win(3)

        return win
