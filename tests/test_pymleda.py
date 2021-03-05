from pymleda import __version__
from pymleda import pymleda
import pandas as pd


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
    ), "The date type of summry should be data frame."

    assert type(pymleda.dftype(df)[1]) == (
        pd.core.frame.DataFrame
    ), "The date type of unique_val should be data frame."

    assert (
        len(pymleda.dftype(df)[0]) == 8
    ), "The length of summary data frame is incorrect."
