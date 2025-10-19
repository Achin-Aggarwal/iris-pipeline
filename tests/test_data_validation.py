import pandas as pd

def test_data_columns():
    df = pd.read_csv("data/iris.csv")
    expected_cols = ["sepal_length", "sepal_width", "petal_length", "petal_width", "species"]
    assert list(df.columns) == expected_cols, "Dataset columns mismatch"

def test_no_missing_values():
    df = pd.read_csv("data/iris.csv")
    assert df.isnull().sum().sum() == 0, "Missing values found in dataset"
