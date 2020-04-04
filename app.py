import os
from flask import Flask, jsonify, request

import numpy as np

from nxn_game import game

app = Flask(__name__)


@app.route("/")
def hello_world():
    target = os.environ.get("TARGET", "World")
    return "Hello {}!\n".format(target)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
