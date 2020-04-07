import os
from flask import Flask, jsonify, request

import numpy as np

import nxn_game.game as game
import nxn_game.utils as utils

app = Flask(__name__)

WEB_PLAYER = game.player.Player(symbol=-1)
GAMEBOARD = game.gameboard.Gameboard()
BOT_PLAYER = utils.save.load_agent("3x3_bot")


@app.route("/player", methods=["POST"])
def player_move():
    moves = request.get_json(force=True, cache=False)
    WEB_PLAYER.make_move(moves["row"], moves["col"], GAMEBOARD, "raw")


@app.route("/bot", methods=["POST"])
def bot_move():
    moves = utils.play.agent_move(BOT_PLAYER, GAMEBOARD, "raw")

    return {"row": moves[0], "col": moves[1]}


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
