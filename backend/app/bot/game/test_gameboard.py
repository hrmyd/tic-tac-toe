import numpy as np

from . import gameboard

ROWS = 3
COLS = 3
WIN_SCORE = 3
GAMEBOARD = gameboard.Gameboard(
    board_id=0, n_rows=ROWS, n_cols=COLS, win_score=WIN_SCORE
)


def test_board_initialization():
    assert GAMEBOARD.board.tolist() == np.zeros((ROWS, COLS)).tolist()


def test_hash():
    assert GAMEBOARD.get_hash() == str(np.zeros(9))


def test_update_board():
    GAMEBOARD.update_board(row=0, col=0, sym=1)
    assert GAMEBOARD.board[0, 0] == 1


def test_check_win_false():
    assert GAMEBOARD.check_win() == False


def test_check_win_true():
    GAMEBOARD.update_board(row=0, col=1, sym=1)
    GAMEBOARD.update_board(row=0, col=2, sym=1)

    assert GAMEBOARD.check_win() == True
    assert GAMEBOARD.winner == 1


def test_reset():
    GAMEBOARD.reset()

    assert GAMEBOARD.board.tolist() == np.zeros((ROWS, COLS)).tolist()
    assert GAMEBOARD.winner == None
    assert GAMEBOARD.hash == None
    assert GAMEBOARD.draw == None
