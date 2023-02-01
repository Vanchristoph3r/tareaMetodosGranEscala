import pandas as pd

from eda import create_plots

COLUMNS_TO_DELETE = [
    "Id",
    "Alley",
    "PoolQC",
    "MiscFeature",
    "Fence",
    "MoSold",
    "YrSold",
    "MSSubClass",
    "GarageType",
    "GarageArea",
    "GarageYrBlt",
    "GarageFinish",
    "YearRemodAdd",
    "LandSlope",
    "BsmtUnfSF",
    "BsmtExposure",
    "2ndFlrSF",
    "LowQualFinSF",
    "Condition1",
    "Condition2",
    "Heating",
    "Exterior1st",
    "Exterior2nd",
    "HouseStyle",
    "LotShape",
    "LandContour",
    "LotConfig",
    "Functional",
    "BsmtFinSF1",
    "BsmtFinSF2",
    "FireplaceQu",
    "WoodDeckSF",
    "GarageQual",
    "GarageCond",
    "OverallCond",
]


def fill_all_missing_values(data: pd.DataFrame) -> pd.DataFrame:
    """Impute missing values with mean if numeric or mode if string

    Args:
        data (pd.DataFrame): _description_
    """
    for col in data.columns:
        if (data[col].dtype == "float64") or (data[col].dtype == "int64"):
            data[col].fillna(data[col].mean(), inplace=True)
        else:
            data[col].fillna(data[col].mode()[0], inplace=True)
    return data


def fill_na_values(data: pd.DataFrame, values: dict) -> pd.DataFrame:
    """Fill NA values for multiple columns

    Args:
        data (pd.DataFrame): dataframe
        values (dict): values in dict form

    Returns:
        pd.DataFrame
    """
    return data.fillna(value=values)


def read_data(path) -> pd.DataFrame:
    """Returns dataframe

    Args:
        path (str): file path to the csv file

    Returns:
        pd.DataFrame
    """
    return pd.read_csv(path)


def delete_cols(cols: list, data: pd.DataFrame) -> pd.DataFrame:
    """Delete cols from dataframe

    Args:
        cols (list): cols to delete
        data (pd.DataFrame): dataframe

    Returns:
        pd.DataFrame:
    """
    return data.drop(cols, axis=1)


def get_data(train_path: str, test_path: str, eda: bool = False) -> list:
    """_summary_

    Args:
        train_path (str): file path
        test_path (str): file path

    Returns:
        list: return dataframes list
    """
    train_data = read_data(train_path)
    test_data = read_data(test_path)
    if eda:
        create_plots(train_data=train_data)

    values = {
        "FireplaceQu": "No",
        "BsmtQual": "No",
        "BsmtCond": "No",
        "BsmtFinType1": "No",
        "BsmtFinType2": "No",
        # "BsmtFinType2": "None",
    }
    train_data = fill_na_values(train_data, values)
    test_data = fill_na_values(test_data, values)

    train_data = fill_all_missing_values(train_data)
    test_data = fill_all_missing_values(test_data)

    train_data = delete_cols(COLUMNS_TO_DELETE, train_data)
    test_data = delete_cols(COLUMNS_TO_DELETE, test_data)

    return train_data, test_data
