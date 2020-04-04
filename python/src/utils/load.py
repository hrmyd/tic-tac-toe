import os

import dill

import nxn_game.game.agent as agent

def load_agent(f_name: str) -> agent.Agent:
    """
    load in an agent from gcp bucket

    Args:
        ``f_name`` (`str`): file name of bot to load
    """
    pass


def save_agent(f_name: str, agent: agent.Agent) -> None:
    """
    save agent to gcp bucket

    Args:
        ``f_name`` (`str`): name of file
        ``agent`` (`agent.Agent`): instance of bot to save
    """
    full_file_name = f"tmp/{f_name}.pkl"

    dill.dump(agent, full_file_name)

    print(f"file {f_name} successfully uploaded to bucket.")
