from pymleda import pymleda
from sklearn.model_selection import train_test_split
import pandas as pd


def test_supervised_data_original_dataset():
    # Simple test to ensure that the data attribute returns the original data unchanged
    toy_data = pd.DataFrame(
        {"col1": [1, 1, 1, 1], "col2": [2, 2, 2, 2], "col3": [3, 3, 3, 3]}
    )

    assert (
        pymleda.SupervisedData(toy_data, x_cols=["col1", "col2"], y_cols=["col3"]).data
        == toy_data
    )


def test_supervised_data_split_sizes():
    # Test that the data splits are of correct sizes

    toy_data = pd.DataFrame(
        {"col1": [1, 1, 1, 1], "col2": [2, 2, 2, 2], "col3": [3, 3, 3, 3]}
    )

    supervised_data = pymleda.SupervisedData(
        toy_data, x_cols=["col1", "col2"], y_cols=["col3"]
    )

    assert len(supervised_data.test_df) == 0.75 * len(toy_data)
    assert len(supervised_data.train_df) == 0.25 * len(toy_data)
