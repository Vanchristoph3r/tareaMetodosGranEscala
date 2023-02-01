import logging
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error


def train_model(train_data: pd.DataFrame) -> RandomForestRegressor:
    """Train and fit a RandomForest Regressor 

    Args:
        train_data (pd.DataFrame): dataframe

    Returns:
        RandomForestRegressor: model
    """    
    y = train_data["SalePrice"]
    X = train_data.drop(["SalePrice"], axis=1)
    candidate_max_leaf_nodes = [250]

    for node in candidate_max_leaf_nodes:
        model = RandomForestRegressor(
            max_leaf_nodes=node,
        )
        model.fit(X, y)
        score = cross_val_score(model, X, y, cv=10)
        logging.info(score.mean())

    return model


def get_predict_values(
    model: RandomForestRegressor, test_data: pd.DataFrame
) -> pd.DataFrame:
    """Get stimation for model

    Args:
        model (RandomForestRegressor): model trained
        test_data (pd.DataFrame): dataframe

    Returns:
        pd.DataFrame: dataframe
    """
    test_ids = test_data["Id"]
    price = model.predict(test_data)
    return pd.DataFrame({"Id": test_ids, "SalePrice": price})
