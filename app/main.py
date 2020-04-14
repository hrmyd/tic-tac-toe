import os
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import numpy as np

import nxn_game.game as game
import nxn_game.utils as utils

### initialize app
app = FastAPI()

### Symbols for board.winner
# 1 = bot
# -1 = player
# 0 = draw
# None = no end game

WEB_PLAYER = game.player.Player(symbol=-1)
GAMEBOARD = game.gameboard.Gameboard()
try:
    BOT_PLAYER = utils.files.load_agent("3x3_bot")
except:
    logging.info("no model found found")


class PlayerMoves(BaseModel):
    row: int
    col: int


@app.post("/player/")
async def player_move(moves: PlayerMoves):
    win = WEB_PLAYER.make_move(moves.row, moves.col, GAMEBOARD, "raw")
    winner = GAMEBOARD.winner
    return {"win": win, "winner": winner}


@app.post("/bot/")
async def bot_move():
    moves, win = utils.play.agent_move(BOT_PLAYER, GAMEBOARD, "raw")
    winner = GAMEBOARD.winner
    return {"row": int(moves[0]), "col": int(moves[1]), "win": win, "winner": winner}
