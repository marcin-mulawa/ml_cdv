import pandas as pd
import matplotlib.pyplot as plt
import os
from typing import Tuple, List

SAVE_DIR = os.path.join(os.getcwd(), "saved")


def create_dataset() -> Tuple[pd.DataFrame, List[int], List[int]]:
    """
    This function returns Anscombe's quartet y_i in pandas Dataframe and x_i in python lists
    Returns:
        anscombe_df : DataFrame of y_i anscombe values
        x: list
        x4: list
    """

    # initialize Anscombe's quartet data
    x = [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5]
    y1 = [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]
    y2 = [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]
    y3 = [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73]
    x4 = [8, 8, 8, 8, 8, 8, 8, 19, 8, 8, 8]
    y4 = [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]

    # create DataFrame from Anscombe's data
    df_dict = {"y1": y1, "y2": y2, "y3": y3, "y4": y4}
    anscombe_df = pd.DataFrame(df_dict, index=x)

    return anscombe_df, x, x4


def calculate_stats(data: pd.DataFrame) -> pd.DataFrame:
    """
    This function calculates mean, standard deviation and variance
    Args:
        data: pd.DataFrame

    Returns:
        describe: pd.DataFrame with calculated mean, std, variance for each column

    """

    describe = data.describe().loc[["mean", "std"]]
    variance = pd.DataFrame({"var": data.var()})
    describe = describe.T.merge(variance, left_index=True, right_index=True)

    return describe


def anscombe_scatter(anscombe_df: pd.DataFrame, x: List[int], x4: List[int]) -> plt.figure:
    """
    Creates 4 scatter charts
    Args:
        anscombe_df: pd.DataFrame
        x: list
        x4: list

    Returns:
        fig: subplot of 4 charts

    """

    # scatter plot of Anscombe's quartet data
    fig, axs = plt.subplots(2, 2, sharex=True, sharey=True, figsize=(6, 5))
    axs[0, 0].set(xlim=(0, 20), ylim=(2, 14))
    axs[0, 0].set(xticks=(0, 10, 20), yticks=(4, 8, 12))
    titles = ["I", "II", "III", "IV"]
    x_labels = ["x", "x", "x", "x4"]
    y_labels = ["y1", "y2", "y3", "y4"]
    x_i = [x, x, x, x4]
    y_i = [anscombe_df["y1"], anscombe_df["y2"], anscombe_df["y3"], anscombe_df["y4"]]
    k = 0
    for i in range(2):
        for j in range(2):
            axs[i, j].scatter(x_i[k], y_i[k])
            axs[i, j].set_title(titles[k])
            axs[i, j].set_xlabel(x_labels[k])
            axs[i, j].set_ylabel(y_labels[k])
            k += 1
    fig.tight_layout()
    return fig


if __name__ == "__main__":
    os.makedirs(SAVE_DIR, exist_ok=True)
    anscombe_df, x, x4 = create_dataset()
    describe = calculate_stats(anscombe_df)
    describe.to_csv(os.path.join(SAVE_DIR, "description.csv"))
    fig = anscombe_scatter(anscombe_df, x, x4)
    fig.savefig(os.path.join(SAVE_DIR, "chart.jpg"))
