import numpy as np

from .. import game

def train_agent(player1, player2, rounds):
  player1_wins = np.zeros(rounds)
  player2_wins = np.zeros(rounds)

  win_score = 3

  for i in range(rounds):
    board = game.Gameboard()
    symbol_map = board.symbols
    print(f"starting round {i+1}")
    while board.winner is None:
      for player in [player1, player2]:
        move = player.move(board)
        board.update_board(move[0], move[1], symbol_map[player.symbol])
        player.update_move_history(board.get_hash())
        winner = board.check_win(win_score)

        # in case player one fills last spot
        if board.winner is not None:
          break

    if winner and board.winner == player1.symbol:
      player1.reward(1)
      player2.reward(-1)
      player1_wins[i] = 1
    elif winner and board.winner == player2.symbol:
      player1.reward(-1)
      player2.reward(1)
      player2_wins[i] = 1
    elif not winner and board.winner == 0:
      player1.reward(-1)
      player2.reward(-1)

    player1.reset()
    player2.reset()

  return player1_wins, player2_wins

def agent_move(player, board):
  if board.winner is None:
    move = player.move(board)
    board.update_board(move[0], move[1], player.symbol)
    player.update_move_history(board.get_hash())

  board.str_rep()
  win = board.check_win(3)

  if win and board.winner == player.symbol:
    player.reward(1)
    player.reset()
  else:
    player.reward(-1)
    player.reset()