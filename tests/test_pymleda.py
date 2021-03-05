import pandas as pd
import numpy as np
import pytest
from pandas.util.testing import assert_frame_equal
from pymleda import pymleda


@pytest.fixture
def model_df():
    """Create the model dataframe with no missing values"""
    choco_data = {
        "Chocolate_brand": ["Lindt", "Rakhat", "Lindt", "Richart", "Lindt"],
        "Price": [3.0, 4.0, 4.0, 6.0, 3.0],
    }
    input = pd.DataFrame(choco_data, columns=["Chocolate_brand", "Price"])
    return input


choco_data_1 = {
    "Chocolate_brand": ["Lindt", "Rakhat", "Lindt", "Richart", "Lindt"],
    "Price": [3.0, 4.0, 4.0, 6.0, 3.0],
}
toy_df_1 = pd.DataFrame(choco_data_1, columns=["Chocolate_brand", "Price"])


choco_data_2 = {
    "Chocolate_brand": ["Lindt", "Rakhat", "Lindt", "Richart", "not available"],
    "Price": [3.0, np.nan, 4.0, 6.0, 3.0],
}
toy_df_2 = pd.DataFrame(choco_data_2, columns=["Chocolate_brand", "Price"])


def test_autoimpute_na_1(model_df):
    """Test that the output dataframe of the pymleda.autoimpute_na() function
    with no missing values is equal to the model dataframe (identical to the original one)"""
    assert_frame_equal(pymleda.autoimpute_na(toy_df_1), model_df)


def test_autoimpute_na_2(model_df):
    """Test that the output dataframe of the pymleda.autoimpute_na() function
    with some missing values is equal to the model dataframe"""
    assert_frame_equal(pymleda.autoimpute_na(toy_df_2), model_df)