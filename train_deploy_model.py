import os
import logging

import numpy as np

from nxn_game import utils
from nxn_game.game import agent

logging.getLogger().setLevel(logging.INFO)


def main():
    training_rounds = 5000
    agent_one = agent.Agent(symbol=1)  # the one we'll save
    agent_two = agent.Agent(symbol=-1)

    logging.info("beginning training")
    wins = utils.play.train_agent(agent_one, agent_two, training_rounds)
    one_win_ratio = np.sum(wins[0]) / (np.sum(wins[0]) + np.sum(wins[1]))
    logging.info("training finished!")
    logging.info(f"bot one won {one_win_ratio:.2%} of the time.")

    utils.files.save_agent("3x3_bot", agent_one)


if __name__ == "__main__":
    main()
