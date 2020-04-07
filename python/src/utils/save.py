import os

import dill

import nxn_game.game.agent as agent


def load_agent(f_name: str) -> agent.Agent:
    """
    load in an agent

    Args:
        ``f_name`` (`str`): file name of bot to load
    """
    full_file_name = f"models/{f_name}.pkl"
    dill.load(agent, full_file_name)


def save_agent(f_name: str, agent: agent.Agent) -> None:
    """
    save agent

    Args:
        ``f_name`` (`str`): name of file
        ``agent`` (`agent.Agent`): instance of bot to save
    """
    full_file_name = f"models/{f_name}.pkl"

    dill.dump(agent, full_file_name)

    print(f"model {f_name} successfully saved.")
