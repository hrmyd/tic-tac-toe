import os
import logging

import numpy as np

from app.bot.utils import play, files
from app.bot.game import agent


def train():
    training_rounds = 5000
    agent_one = agent.Agent(symbol=1)  # the one we'll save
    agent_two = agent.Agent(symbol=-1)

    logging.info("beginning training")
    wins = play.train_agent(agent_one, agent_two, training_rounds)
    one_win_ratio = np.sum(wins[0]) / (np.sum(wins[0]) + np.sum(wins[1]))
    logging.info("training finished!")
    logging.info(f"bot one won {one_win_ratio:.2%} of the time.")

    files.save_agent("3x3_bot", agent_one)
