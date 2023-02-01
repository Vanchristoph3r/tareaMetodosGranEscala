import logging
import pandas as pd

from clean_data import delete_cols
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder

import pdb

COLS_TO_DROP = [
    "OverallQual",
    "ExterCond",
    "ExterQual",
    "BsmtCond",
    "BsmtQual",
    "BsmtFinType1",
    "BsmtFinType2",
    "HeatingQC",
    "OpenPorchSF",
    "EnclosedPorch",
    "3SsnPorch",
    "ScreenPorch",
    "BsmtFullBath",
    "BsmtHalfBath",
    "FullBath",
    "HalfBath",
]


def encode_label_columns(
    columns: list, train: pd.DataFrame, test: pd.DataFrame
) -> list:
    """Encodes variable

    Args:
        columns (list): cols to encode
        train (pd.DataFrame): dataset
        test (pd.DataFrame): dataset

    Returns:
        list: list of datasets
    """
    _encoder = LabelEncoder()
    for col in columns:
        train[col] = _encoder.fit_transform(train[col])
        test[col] = _encoder.transform(test[col])
    return train, test


def encode_categorical_columns(
    categories: list,
    column: str,
    train: pd.DataFrame,
    test: pd.DataFrame,
) -> list:
    """Encodes categorical variables

    Args:
        categories (list): _description_
        column (str): _description_
        train (pd.DataFrame): _description_
        test (pd.DataFrame): _description_

    Returns:
        list: _description_
    """
    _encoder = OrdinalEncoder(categories=[categories])
    train[column] = _encoder.fit_transform(train[[column]])
    test[column] = _encoder.transform(test[[column]])
    return train, test


def product_of_columns(data: pd.DataFrame, cols: list) -> pd.DataFrame:
    data = data.iloc[data[cols[1]] * data[cols[2]], cols[0]]
    return data


def sum_columns(data: pd.DataFrame, cols: list) -> pd.DataFrame:
    data = data.iloc[data[cols[1]] + data[cols[2]], cols[0]]
    return data


def encode_data(train: pd.DataFrame, test: pd.DataFrame) -> list:
    """Encodes categorical or label columns

    Args:
        train (pd.DataFrame): dataframe
        test (pd.DataFrame): dataframe

    Returns:
        list: list of dataframes
    """
    cols_1 = ["No", "Po", "Fa", "TA", "Gd", "Ex"]
    cols_2 = ["Po", "Fa", "TA", "Gd", "Ex"]
    cols_3 = ["N", "P", "Y"]
    cols_4 = ["No", "Unf", "LwQ", "Rec", "BLQ", "ALQ", "GLQ"]
    cols_5 = ["ELO", "NoSeWa", "NoSewr", "AllPub"]
    cols_6 = ["C (all)", "RH", "RM", "RL", "FV"]
    cols_7 = ["Slab", "BrkTil", "Stone", "CBlock", "Wood", "PConc"]
    cols_8 = [
        "MeadowV",
        "IDOTRR",
        "BrDale",
        "Edwards",
        "BrkSide",
        "OldTown",
        "NAmes",
        "Sawyer",
        "Mitchel",
        "NPkVill",
        "SWISU",
        "Blueste",
        "SawyerW",
        "NWAmes",
        "Gilbert",
        "Blmngtn",
        "ClearCr",
        "Crawfor",
        "CollgCr",
        "Veenker",
        "Timber",
        "Somerst",
        "NoRidge",
        "StoneBr",
        "NridgHt",
    ]
    cols_9 = ["None", "BrkCmn", "BrkFace", "Stone"]
    cols_10 = ["AdjLand", "Abnorml", "Alloca", "Family", "Normal", "Partial"]
    cols_11 = ["Gambrel", "Gable", "Hip", "Mansard", "Flat", "Shed"]
    cols_12 = [
        "ClyTile",
        "CompShg",
        "Roll",
        "Metal",
        "Tar&Grv",
        "Membran",
        "WdShake",
        "WdShngl",
    ]
    cols_13 = ["Mix", "FuseP", "FuseF", "FuseA", "SBrkr"]

    level_cols = ["Street", "BldgType", "SaleType", "CentralAir"]

    cols_to_encode = {
        "BsmtQual": cols_1,
        "BsmtCond": cols_1,
        "ExterQual": cols_2,
        "ExterCond": cols_2,
        "KitchenQual": cols_2,
        "PavedDrive": cols_3,
        "Electrical": cols_13,
        "BsmtFinType1": cols_4,
        "BsmtFinType2": cols_4,
        "Utilities": cols_5,
        "MSZoning": cols_6,
        "Foundation": cols_7,
        "Neighborhood": cols_8,
        "MasVnrType": cols_9,
        "SaleCondition": cols_10,
        "RoofStyle": cols_11,
        "RoofMatl": cols_12,
    }

    for key, val in cols_to_encode.items():
        print(key)
        print(val)
        train, test = encode_categorical_columns(
            categories=val, column=key, train=train, test=test
        )

    train, test = encode_label_columns(level_cols, train, test)

    cols_to_mutate = {
        "train": {
            product_of_columns: [
                ["BsmtRating", "BsmtCond", "BsmtQual"],
                ["ExterRating", "ExterCond", "ExterQual"],
                ["BsmtFinTypeRating", "BsmtFinType1", "BsmtFinType2"],
            ],
            sum_columns: [
                ["BsmtBath", "BsmtFullBath", "BsmtHalfBath"],
                ["Bath", "FullBath", "HalfBath"],
                [
                    "PorchArea",
                    "OpenPorchSF",
                    "EnclosedPorch",
                    "3SsnPorch",
                    "ScreenPorch",
                ],
            ],
        },
        "test": {
            product_of_columns: [
                ["BsmtRating", "BsmtCond", "BsmtQual"],
                ["ExterRating", "ExterCond", "ExterQual"],
                ["BsmtFinTypeRating", "BsmtFinType1", "BsmtFinType2"],
            ],
            sum_columns: [
                ["BsmtBath", "BsmtFullBath", "BsmtHalfBath"],
                ["Bath", "FullBath", "HalfBath"],
                [
                    "PorchArea",
                    "OpenPorchSF",
                    "EnclosedPorch",
                    "3SsnPorch",
                    "ScreenPorch",
                ],
            ],
        },
    }
    # cols_to_mutate = {
    #     "product_cols_train": {
    #         "cols": [
    #             ["BsmtRating", "BsmtCond", "BsmtQual"],
    #             ["ExterRating", "ExterCond", "ExterQual"],
    #             ["BsmtFinTypeRating", "BsmtFinType1", "BsmtFinType2"],
    #         ],
    #         "func": product_of_columns,
    #     },
    #     "product_cols_test": {
    #         "cols": [
    #             ["BsmtRating", "BsmtCond", "BsmtQual"],
    #             ["ExterRating", "ExterCond", "ExterQual"],
    #             ["BsmtFinTypeRating", "BsmtFinType1", "BsmtFinType2"],
    #         ],
    #         "func": product_of_columns,
    #     },
    #     "sum_cols_train": {
    #         "cols": [
    #             ["BsmtBath", "BsmtFullBath", "BsmtHalfBath"],
    #             ["Bath", "FullBath", "HalfBath"],
    #             [
    #                 "PorchArea",
    #                 "OpenPorchSF",
    #                 "EnclosedPorch",
    #                 "3SsnPorch",
    #                 "ScreenPorch",
    #             ],
    #         ],
    #         "func": sum_columns,
    #     },
    #     "sum_cols_test": {
    #         "cols": [
    #             ["BsmtBath", "BsmtFullBath", "BsmtHalfBath"],
    #             ["Bath", "FullBath", "HalfBath"],
    #             [
    #                 "PorchArea",
    #                 "OpenPorchSF",
    #                 "EnclosedPorch",
    #                 "3SsnPorch",
    #                 "ScreenPorch",
    #             ],
    #         ],
    #         "func": sum_columns,
    #     },
    # }

    # Sum or product of the columns to mutate
    for name, vals in cols_to_mutate.items():
        for cols in vals:
            if "train" in name:
                train = vals["func"](train, cols)
            else:
                test = vals["func"](test, cols)

    # Delete columns after mutatations and transformations
    train = delete_cols(cols=COLS_TO_DROP, data=test)
    test = delete_cols(cols=COLS_TO_DROP, data=test)

    return train, test
