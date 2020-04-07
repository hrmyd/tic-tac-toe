import os
from flask import Flask, jsonify, request

import numpy as np

import nxn_game.game as game
import nxn_game.utils as utils

app = Flask(__name__)


### Symbols for board.winner
# 1 = bot
# -1 = player
# 0 = draw
# None = no end game


WEB_PLAYER = game.player.Player(symbol=-1)
GAMEBOARD = game.gameboard.Gameboard()
BOT_PLAYER = utils.save.load_agent("3x3_bot")


@app.route("/player", methods=["POST"])
def player_move():
    moves = request.get_json(force=True, cache=False)
    win = WEB_PLAYER.make_move(moves["row"], moves["col"], GAMEBOARD, "raw")
    winner = GAMEBOARD.winner

    return jsonify(win=win, winner=winner)


@app.route("/bot", methods=["GET"])
def bot_move():
    moves, win = utils.play.agent_move(BOT_PLAYER, GAMEBOARD, "raw")
    winner = GAMEBOARD.winner

    return jsonify(row=moves[0], col=moves[1], win=win, winner=winner)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
