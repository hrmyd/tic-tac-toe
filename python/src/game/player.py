import numpy as np
import pandas as pd

from .gameboard import Gameboard

class Player:
    def __init__(self, symbol: int) -> None:
        self.symbol = symbol

    def make_move(self, row: int, col: int, board: Gameboard) -> None:
        board.update_board(row, col, self.symbol)

        board.str_rep()
        board.check_win(3)
