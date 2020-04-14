import os
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import numpy as np

from .bot import game, utils

### initialize app
app = FastAPI(title="Tic Tac Toe")

### Symbols for board.winner
# 1 = bot
# -1 = player
# 0 = draw
# 2 = no end game

WEB_PLAYER = game.player.Player(symbol=-1)
GAMEBOARD = game.gameboard.Gameboard()
BOT_PLAYER = utils.files.load_agent("3x3_bot")


class PlayerMoves(BaseModel):
    row: int
    col: int

class PlayerResponse(BaseModel):
    win: bool
    winner: int

class BotResponse(BaseModel):
    win: bool
    winner: int
    row: int
    col: int


@app.get("/")
def read_root():
    return {"player symbol": WEB_PLAYER.symbol}


@app.post("/move/player", response_model=PlayerResponse)
def player_move(moves: PlayerMoves):
    win = WEB_PLAYER.make_move(moves.row, moves.col, GAMEBOARD, "raw")
    winner = GAMEBOARD.winner

    if winner is None:
        winner = 2

    return {"win": win, "winner": winner}


@app.post("/move/bot", response_model=BotResponse)
def bot_move():
    moves, win = utils.play.agent_move(BOT_PLAYER, GAMEBOARD, "raw")
    winner = GAMEBOARD.winner

    if winner is None:
        winner = 2

    return {"row": int(moves[0]), "col": int(moves[1]), "win": win, "winner": winner}
