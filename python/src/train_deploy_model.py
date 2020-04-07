import os

from . import utils
from .game import agent


def main():
    training_rounds = 5000
    agent_one = agent.Agent(symbol=1)  # the one we'll save
    agent_two = agent.Agent(symbol=-1)

    print("beginning training")
    wins = utils.play.train_agent(agent_one, agent_two, training_rounds)
    one_win_ratio = np.sum(wins[0]) / (np.sum(wins[0]) + np.sum(wins[1]))
    print(f"bot one won {one_win_ratio:.2%} of the time.")

    utils.save.save_agent("3x3_bot", agent_one)


if __name__ == "__main__":
    main()
