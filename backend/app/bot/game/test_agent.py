import numpy as np

from . import player
from . import gameboard
from . import agent


PLAYER = player.Player(symbol=-1)
BOARD = gameboard.Gameboard(board_id=0)
AGENT = agent.Agent(symbol=1)


def test_move():
    move = AGENT.move(BOARD)

    assert move.shape == (2,)
    assert move[0] < 3
    assert move[0] >= 0
    assert move[1] < 3
    assert move[1] >= 0


def test_update_move_history():
    board_hash = BOARD.get_hash()
    AGENT.update_move_history(board_hash)

    assert AGENT.moves_taken == [board_hash]


def test_get_values():
    pass


def test_reward():
    AGENT.reward(1)
    board_hash = BOARD.get_hash()

    assert AGENT.states == {board_hash: 0.020000000000000004}


def test_reset():
    AGENT.reset()

    assert AGENT.moves_taken == []
