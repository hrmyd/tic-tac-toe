import numpy as np
import pandas as pd

class Agent:
  def __init__(self, symbol, lr=0.2, exp_rate=0.4, discount_factor=0.1):
    """
    initialize a player and associated symbol.
    learning rate,
    exploration rate,
    discount factor
    """
    self.symbol = symbol
    self.lr = lr
    self.exp_rate = exp_rate
    self.discount_factor = discount_factor
    self.states = {}
    self.moves_taken = []

  def _get_values(self, hash):
    """
    """
    if hash not in self.states:
      values = 0
    else:
      values = self.states[hash]

    return values

  def move(self, board):
    """
    choose next move
    """
    explore = np.random.uniform(0, 1) < self.exp_rate
    avail_idx = np.argwhere(board.board == 0)
    next_move = None
    
    if explore: # look through all available positions and find best move
      max_value = -999
      for pos in avail_idx:
        next_board = deepcopy(board)
        next_board.update_board(pos[0], pos[1], self.symbol)
        board_hash = next_board.get_hash()
        value = self._get_values(board_hash)

        if value > max_value:
          max_value = value
          next_move = pos
    else:
      pos_idx = np.random.randint(len(avail_idx))
      next_move = avail_idx[pos_idx]

    return next_move

  def update_move_history(self, board_hash):
    """
    add move to front of the list.
    """
    self.moves_taken.insert(0, board_hash)

  def reward(self, reward):
    """
    update rewards at end of game for each state.

    Q(S,A)= Q(S,A)+α∗(γ∗maxaQ(S′,a)− Q(S,A))
    """
    # move history is reversed, reward is reward for the next move taken
    for move in self.moves_taken:
      if move not in self.states:
        self.states[move] = 0
      self.states[move] += self.lr * (self.discount_factor * reward - self.states[move])
      reward = self.states[move]

  def reset(self):
    """
    """
    self.moves_taken = []
