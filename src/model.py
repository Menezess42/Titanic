# Ariel A. O. Menezes
# Imports
from pathlib import Path
from pprint import pprint

import numpy as np
import pandas as pd

# Global constants
BASE_PATH = Path(__file__).parent.parent
DATA_PATH = Path(__file__).parent.parent / "data"

# Global config
pd.set_option("display.max_columns", None)


def show_data(data: pd.DataFrame, n: int = 10) -> None:
    """
    Show the <n>th number of lines of the data.
    input:
        data: pd.DataFrame -- data to be show;
        n: int default 10 -- number of lines to show;
    """
    pprint(data[:n])


if __name__ == "__main__":
    train = pd.read_csv(f"{DATA_PATH}/train.csv")
    test = pd.read_csv(f"{DATA_PATH}/test.csv")
    print("Train data")
    show_data(data=train)
    print("Test data")
    show_data(data=test)
