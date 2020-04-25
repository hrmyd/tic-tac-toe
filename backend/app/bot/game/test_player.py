import numpy as np

from . import player
from . import gameboard


PLAYER = player.Player(symbol=-1)
BOARD = gameboard.Gameboard(board_id=0)


def test_make_move():
    win = PLAYER.make_move(row=0, col=1, board=BOARD)

    assert win == False
    assert BOARD.board.tolist() == np.array([[0, -1, 0], [0, 0, 0], [0, 0, 0]]).tolist()
