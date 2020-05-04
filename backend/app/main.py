import os
import logging
from enum import Enum

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import numpy as np

from .bot import game, utils

### initialize app
app = FastAPI(
    title="Tic Tac Toe",
    description="adventures in python APIs and javascript",
    docs_url=None,
    redoc_url="/docs",
)

origins = ["https://tic-tac-toe.hrmyd.me/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

### Symbols for board.winner
# 1 = bot
# -1 = player
# 0 = draw
# 2 = no end game

WEB_PLAYER = game.player.Player(symbol=-1)
GAMEBOARDS = {}
BOT_PLAYER = utils.files.load_agent("3x3_bot")


class BoardInit(BaseModel):
    rows: int
    cols: int
    score: int


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


@app.post("/new-game/{game_id}")
def initialize_game(*, game_id: int, board_features: BoardInit):
    gameboard = game.gameboard.Gameboard(
        board_id=game_id,
        n_rows=board_features.rows,
        n_cols=board_features.cols,
        win_score=board_features.score,
    )
    GAMEBOARDS[game_id] = gameboard


@app.post("/move/player/{game_id}", response_model=PlayerResponse)
def player_move(*, game_id: int, moves: PlayerMoves):
    board = GAMEBOARDS[game_id]
    win = WEB_PLAYER.make_move(moves.row, moves.col, board, "raw")
    winner = board.winner

    if winner is None:
        winner = 2

    return {"win": win, "winner": winner}


@app.post("/move/bot/{game_id}", response_model=BotResponse)
def bot_move(game_id: int):
    board = GAMEBOARDS[game_id]
    moves, win = utils.play.agent_move(BOT_PLAYER, board, "raw")
    winner = board.winner

    if winner is None:
        winner = 2

    return {"row": int(moves[0]), "col": int(moves[1]), "win": win, "winner": winner}


@app.get("/game-over/{game_id}")
def game_over(game_id: int):
    board = GAMEBOARDS[game_id]
    board.reset()

    return {"status": "gameboard reset, let's play again"}
