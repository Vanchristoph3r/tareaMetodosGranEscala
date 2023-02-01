"""Main executor"""
import logging
import sys
import yaml

from src.estimation import get_estimation

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)


def load_config() -> dict:
    """Loads yaml config

    Returns:
        dict: dict of config vars
    """
    with open("config.yaml", "r") as file:
        config = yaml.safe_load(file)
    return config


if __name__ == "__main__":
    get_estimation(load_config())
