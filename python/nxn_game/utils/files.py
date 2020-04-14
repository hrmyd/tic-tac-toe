import os
import logging

import dill

import nxn_game.game.agent as agent


def load_agent(f_name: str) -> agent.Agent:
    """
    load in an agent

    Args:
        ``f_name`` (`str`): file name of bot to load
    """
    full_file_name = f"./models/{f_name}.pkl"
    with open(full_file_name, "rb") as f:
        bot = dill.load(f)

    logging.info(f"model {full_file_name} successfully loaded.")

    return bot


def save_agent(f_name: str, agent: agent.Agent) -> None:
    """
    save agent

    Args:
        ``f_name`` (`str`): name of file
        ``agent`` (`agent.Agent`): instance of bot to save
    """
    full_file_name = f"./models/{f_name}.pkl"

    with open(full_file_name, "wb") as f:
        dill.dump(agent, f)

    logging.info(f"model {full_file_name} successfully saved.")
