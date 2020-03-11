import numpy as np
import pandas as pd

class Player:
  def __init__(self, symbol):
    self.symbol = symbol

  def make_move(self, row, col, board):
    board.update_board(row, col, self.symbol)

    board.str_rep()
    board.check_win(3)
    