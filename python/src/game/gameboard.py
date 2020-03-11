import numpy as np
import pandas as pd

class Gameboard:
  def __init__(self, n_rows=3, n_cols=3):
    self.n_rows = n_rows
    self.n_cols = n_cols
    self.board = np.zeros((self.n_rows, self.n_cols))
    self.symbols = {0: " ", 1: "X", -1: "O"}
    self.symbols_rev = {" ": 0, "X": 1, "O": -1}
    self.winner = None
    self.draw = None 
    self.hash = None

  def str_rep(self):
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

  def get_hash(self):
    """
    basically, return flattened view of board
    """
    self.hash = str(self.board.flatten())
    return self.hash

  def update_board(self, row, col, sym):
    """
    update array with int representation of symbol if position is valid.
    """
    if not isinstance(sym, int):
      sym = self.symbols_rev[sym]

    if self.board[row, col] == 0:
      self.board[row, col] = sym
    else:
      print("move not valid, space not empty")

  def check_win(self, win_score):
    """
    check diagonals, rows, and columns for win_score (+ or -) or draw.
    """
    left_diag_score = np.sum(np.diag(self.board))
    right_diag_score = np.sum(np.diag(np.fliplr(self.board)))

    row_sums = np.sum(self.board, axis=1)
    col_sums = np.sum(self.board, axis=0)

    x_win =  win_score
    o_win = win_score * -1

    # check if x wins
    if x_win in row_sums or x_win in col_sums or x_win in [left_diag_score, right_diag_score]:
      self.winner = 1
      print("game over, X wins")
      return True

    # check if o wins
    if o_win in row_sums or o_win in col_sums or o_win in [left_diag_score, right_diag_score]:
      self.winner = -1
      print("game over, O wins")
      return True

    # check if draw
    if 0 not in self.board:
      self.draw = True
      self.winner = 0
      print("game over, draw")
      return False
    
    return False

  def reset(self):
    """
    back to square one
    """
    self.board = np.zeros((self.n_rows, self.n_cols))
    self.winner = None
    self.draw = None 
    self.hash = None
    