import os

from . import utils
from .game import agent


def main():
    training_rounds = 2000
    agent_one = agent.Agent(symbol=1)  # the one we'll save
    agent_two = agent.Agent(symbol=-1)

    wins = utils.play.train_agent(agent_one, agent_two, training_rounds)

if __name__ == "__main__":
    main()
