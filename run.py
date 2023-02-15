"""Main executor"""
import argparse
import logging
import sys
import yaml


from src.estimation import get_estimation

parser = argparse.ArgumentParser(
    prog="Trainmodel", 
    usage="use: %(prog)s [-f] file_to_config",
    description="Trains house model prediction")
parser.add_argument("-f", "--file", type=str)
args = parser.parse_args()

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)


def load_config(file_path: str) -> dict:
    """Loads yaml config

    Returns:
        dict: dict of config vars
    """
    with open(file_path, "r") as file:
        config = yaml.safe_load(file)
    return config


if __name__ == "__main__":
    if args.file:
        file_path = args.file
        logging.info("File path args %s", file_path)
    else:
        file_path = "config.yaml"

    get_estimation(load_config(file_path))
