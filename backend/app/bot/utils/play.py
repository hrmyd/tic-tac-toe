from typing import Tuple
import logging

import numpy as np


from ..game import gameboard, agent


def train_agent(
    player1: agent.Agent, player2: agent.Agent, rounds: int
) -> Tuple[np.array, np.array]:
    """
    Train the bots! Make two bots play against each other for X rounds.
    Makes for a smarter bot to play against :)

    Args:
        ``player1`` (`agent.Agent`): first bot instance
        ``player2`` (`agent.Agent`): second bot instance
        ``rounds`` (`int`): number of rounds for play

    Returns:
        `tuple`: Number of wins for player one and player two
    """
    player1_wins = np.zeros(rounds)
    player2_wins = np.zeros(rounds)

    win_score = 3

    for i in range(rounds):
        board = gameboard.Gameboard()
        symbol_map = board.symbols
        # logging.info(f"starting round {i+1}")
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

    logging.info(f"trained with {rounds} rounds.")
    return player1_wins, player2_wins


def agent_move(
    player: agent.Agent, board: gameboard.Gameboard, board_type: str = "string"
) -> Tuple[np.array, bool]:
    """
    Creates move for bot, updates history, checks for win, and updates
    reward as necessary.

    Args:
        ``player`` (`agent.Agent`): player instance, in this case the bot
        ``board`` (`gameboard.Gameboard`): game board instance

    Returns:
        `tuple`: moves for bot and if winning move
    """
    if board.winner is None:
        move = player.move(board)
        board.update_board(move[0], move[1], player.symbol)
        player.update_move_history(board.get_hash())

    if board_type == "string":
        board.str_rep()

    win = board.check_win(3)

    if win and board.winner == player.symbol:
        player.reward(1)
        player.reset()
    elif win and board.winner != player.symbol:
        player.reward(-1)
        player.reset()
    elif not win and board.winner == 0:
        player.reward(-1)
        player.reset()

    return move, win
