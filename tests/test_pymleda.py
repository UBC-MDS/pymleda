from pymleda import pymleda
import pandas as pd
import numpy as np
import pytest


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
    "Chocolate_brand": [
        "Lindt",
        "Rakhat",
        "Lindt",
        "Richart",
        "not available",
    ],
    "Price": [3.0, np.nan, 4.0, 6.0, 3.0],
}
toy_df_2 = pd.DataFrame(choco_data_2, columns=["Chocolate_brand", "Price"])


def test_autoimpute_na_1(model_df):
    """Test that the output dataframe of the pymleda.autoimpute_na() function
    with no missing values is equal to the model dataframe
    (identical to the original one)"""
    pd.testing.assert_frame_equal(pymleda.autoimpute_na(toy_df_1), model_df)


def test_autoimpute_na_2(model_df):
    """Test that the output dataframe of the pymleda.autoimpute_na() function
    with some missing values is equal to the model dataframe"""
    pd.testing.assert_frame_equal(pymleda.autoimpute_na(toy_df_2), model_df)


def test_autoimpute_na_3(model_df):
    """Test that the input of the pymleda.autoimpute_na()
    function is not a dataframe"""
    with pytest.raises(Exception):
        pymleda.SupervisedData(pymleda.autoimpute_na(777), model_df)


def test_dftype():
    """Test that the dftupe works properly. This test will examine the data type of
    input and output. Furthermore, it will check the output is corret."""

    df = pd.DataFrame(
        {
            "type": ["Air", "Ship", "Bus", "Air"],
            "time": [6, 32, 31, 5],
            "origin": ["US", "Mexico", "CANADA", "UK"],
        }
    )

    assert type(df) == (
        pd.core.frame.DataFrame
    ), "The date type of input should be data frame."

    assert type(pymleda.dftype(df)[0]) == (
        pd.core.frame.DataFrame
    ), "The date type of summary should be data frame."

    assert type(pymleda.dftype(df)[1]) == (
        pd.core.frame.DataFrame
    ), "The date type of unique_val should be data frame."

    assert (
        len(pymleda.dftype(df)[0]) == 8
    ), "The length of summary data frame is incorrect."

    assert (
        (
            list(
                pymleda.dftype(df)[1]
                .query("column_name == 'origin'")
                .unique_values
            )
        )
        == df["origin"].unique()
    ).all(), "The unique values are incorrect."

    with pytest.raises(Exception):
        pymleda.dftype(1)


def test_dfscaling():

    df = pd.DataFrame(
        {
            "song_name": ["song1", "song2", "song3", "song4"],
            "acousticness": [5, 5, 5, 5],
            "danceability": [0, 0, 1, 1],
            "duration_ms": [2, 2, 4, 4],
        }
    )

    scaled_df = pd.DataFrame(
        {
            "acousticness": [0.0, 0.0, 0.0, 0.0],
            "danceability": [-1.0, -1.0, 1.0, 1.0],
            "duration_ms": [-1.0, -1.0, 1.0, 1.0],
        }
    )

    assert type(df) == (
        pd.core.frame.DataFrame
    ), "The date type of input should be a pandas data frame."

    assert len(list(df.select_dtypes(include=[np.number]))) != (
        0
    ), "There should be at least one numeric column in the input dataframe."

    # checking that the results of the transformation are as expected
    pd.testing.assert_frame_equal(pymleda.dfscaling(df), scaled_df)
