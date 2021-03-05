from pymleda import __version__
from pymleda import pymleda
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def test_version():
    assert __version__ == "0.1.0"


def test_dftype():

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
        (list(pymleda.dftype(df)[1].query("column_name == 'origin'").unique_values))
        == df["origin"].unique()
    ).all(), "The unique values are incorrect."


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
