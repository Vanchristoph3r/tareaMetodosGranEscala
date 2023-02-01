import seaborn as sns
import pandas as pd

from matplotlib import pyplot as plt


def create_plots(train_data: pd.DataFrame):
    """Create plots for EDA 

    Args:
        train_data (pd.DataFrame): dataframe
    """    
    fig, ax = plt.subplots(figsize=(25, 10))
    sns.heatmap(data=train_data.isnull(), yticklabels=False, ax=ax)
    plt.savefig("heat-map.png")

    fig, ax = plt.subplots(figsize=(25, 10))
    sns.countplot(x=train_data["SaleCondition"])
    sns.histplot(x=train_data["SaleType"], kde=True, ax=ax)
    sns.violinplot(x=train_data["HouseStyle"], y=train_data["SalePrice"], ax=ax)
    sns.scatterplot(
        x=train_data["Foundation"], y=train_data["SalePrice"], palette="deep", ax=ax
    )
    plt.grid()
    plt.savefig("histogram.png")
