from pymleda import pymleda
from sklearn.model_selection import train_test_split
import pandas as pd


def test_supervised_data_original_dataset():
    # Simple test to ensure that the data attribute returns the original data unchanged
    toy_data = pd.DataFrame(
        {"col1": [1, 1, 1, 1], "col2": [2, 2, 2, 2], "col3": [3, 3, 3, 3]}
    )

    assert pymleda.SupervisedData(toy_data).data == toy_data
