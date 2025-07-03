# Titanic kaggle
# ----------------------------
# Ariel Menezes
# github.com/Menezess42
# linkedin.com/in/menezess42
# youtube.com/@Dwarf_Software
# create at: 07-03-2025 18h03

# The import description and anotation you can find in the "Python data science libe information.md"
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from pathlib import Path
from cli.cli import analyze_data
from sklearn.compose import make_column_transformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import (
    GridSearchCV,
    StratifiedKFold,
    cross_val_score,
    train_test_split,
)
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.preprocessing import OrdinalEncoder
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

# GLOBAL CONSTANTS
BASE_PATH = Path(__file__).parent.parent
DATA_PATH = Path(__file__).parent.parent / "data"


# Importing
train_df = pd.read_csv(f"{DATA_PATH}/train.csv")
test_df = pd.read_csv(f"{DATA_PATH}/test.csv")

# Showing train and test heads
analyze_data(train_df)

# Loking into the information
train_df.info()
