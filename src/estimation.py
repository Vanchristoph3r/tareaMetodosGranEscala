""" Estimation module, gathers functions from other modules"""
import logging

from src.clean_data import get_data
from src.model import train_model, get_predict_values
from src.preprocessing import encode_data


def get_estimation(config: dict):
    """
    Loads, transform and get trained model

    Args:
        config (dict): dict with config variables
    """

    # get vars from config
    train_path = config.get("main", {}).get("train_path")
    test_path = config.get("main", {}).get("test_path")
    output_path = config.get("main", {}).get("output_path")
    eda = config.get("main", {}).get("eda", False)

    # get data
    logging.info("Load data")
    train, test = get_data(train_path=train_path, test_path=test_path, eda=eda)
    test_ids = test["Id"]

    # transform data
    logging.info("Transform data")
    train, test = encode_data(train=train, test=test)

    # fit and train
    logging.info("Train and fit data")
    model = train_model(train_data=train)
    predited_values = get_predict_values(model=model, test_ids=test_ids, test_data=test)

    logging.info("Save result to %s", output_path)
    # save
    predited_values.to_csv(output_path, index=False)
