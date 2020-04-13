from typing import Dict, List, Union
from copy import deepcopy

import numpy as np
import pandas as pd

from . import gameboard as game


class Agent:
    def __init__(
        self,
        symbol: int,
        lr: float = 0.2,
        exp_rate: float = 0.4,
        discount_factor: float = 0.1,
    ) -> None:
        """
        initialize a player and associated symbol.

        Args:
            ``symbol`` (`int`): 1 or -1, in a game should be different for
                each player.
            ``lr`` (`float`): the learning rate, basically how quickly will the bot
                learn from moves.
            ``exp_rate`` (`float`): exploration rate, how often will bot explore moves
                vs making a random move.
            ``discount_factor`` (`float`): weight future reward impact.
        """
        self.symbol = symbol
        self.lr = lr
        self.exp_rate = exp_rate
        self.discount_factor = discount_factor
        self.states: Dict[str, float] = {}
        self.moves_taken: List[str] = []

    def _get_values(self, hash: str) -> float:
        """
        checks if move has been made before. if not,
        initialize in move dictionary. otherwise, return
        current value of making that move.

        Args:
            ``hash`` (`str`): representation of board.
        
        Returns:
            ``values`` (`float`): value stored for a move.
        """
        if hash not in self.states:
            values = 0.0
        else:
            values = self.states[hash]

        return values

    def move(self, board: game.Gameboard) -> np.array:
        """
        choose next move.

        Args:
            ``board`` (`game.Gameboard`): current instance of gameboard.

        Returns:
            `np.array`: index of next move in gameboard.
        """
        explore = np.random.uniform(0, 1) < self.exp_rate
        avail_idx = np.argwhere(board.board == 0)
        next_move = None

        if explore:  # look through all available positions and find best move
            max_value: Union[float, int] = -999
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

    def update_move_history(self, board_hash: str) -> None:
        """
        add move to front of the list.

        Args:
            ``board_hash`` (`str`): str represantation of move on board.
        """
        self.moves_taken.insert(0, board_hash)

    def reward(self, reward: Union[int, float]) -> None:
        """
        update rewards at end of game for each state.

            ``Q(S,A)= Q(S,A)+α∗(γ∗maxaQ(S′,a)− Q(S,A))``

        Args:
            ``reward`` (`int` or `float`): reward to initialize with.
        """
        # move history is reversed, reward is reward for the next move taken
        for move in self.moves_taken:
            if move not in self.states:
                self.states[move] = 0
            self.states[move] += self.lr * (
                self.discount_factor * reward - self.states[move]
            )
            reward = self.states[move]

    def reset(self) -> None:
        """
        back to square one.
        """
        self.moves_taken = []
