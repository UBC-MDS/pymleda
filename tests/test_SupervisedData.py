from pymleda import pymleda
import pandas as pd
import pytest


def test_supervised_data_original_dataset():
    # Simple test to ensure that the data attribute returns the original
    # data unchanged
    toy_data = pd.DataFrame(
        {"col1": [1, 1, 1, 1], "col2": [2, 2, 2, 2], "col3": [3, 3, 3, 3]}
    )

    assert (
        pd.testing.assert_frame_equal(
            pymleda.SupervisedData(
                toy_data, x_cols=["col1", "col2"], y_cols=["col3"]
            ).data,
            toy_data,
        )
        is None
    )


def test_supervised_data_split_sizes():
    # Test that the data splits are of correct sizes

    toy_data = pd.DataFrame(
        {"col1": [1, 1, 1, 1], "col2": [2, 2, 2, 2], "col3": [3, 3, 3, 3]}
    )

    supervised_data = pymleda.SupervisedData(
        toy_data, x_cols=["col1", "col2"], y_cols=["col3"]
    )

    assert len(supervised_data.test_df) == 0.25 * len(toy_data)
    assert len(supervised_data.train_df) == 0.75 * len(toy_data)

    # Reconstruct the original dataframe from the two subsets as a second check
    reconstructed = pd.concat(
        [supervised_data.test_df, supervised_data.train_df]
    )

    assert (
        pd.testing.assert_frame_equal(
            reconstructed,
            toy_data,
            check_like=True,
        )
        is None
    )


def test_supervised_data_x():
    # Test that the x portions of the data only contain the x columns

    toy_data = pd.DataFrame(
        {"col1": [1, 1, 1, 1], "col2": [2, 2, 2, 2], "col3": [3, 3, 3, 3]}
    )

    supervised_data = pymleda.SupervisedData(
        toy_data, x_cols=["col1", "col2"], y_cols=["col3"]
    )

    assert list(supervised_data.x_train.columns) == ["col1", "col2"]
    assert list(supervised_data.x_test.columns) == ["col1", "col2"]


def test_supervised_data_y():
    # Test that the y portions of the data only contain the y columns

    toy_data = pd.DataFrame(
        {"col1": [1, 1, 1, 1], "col2": [2, 2, 2, 2], "col3": [3, 3, 3, 3]}
    )

    supervised_data = pymleda.SupervisedData(
        toy_data, x_cols=["col1", "col2"], y_cols=["col3"]
    )

    assert list(supervised_data.y_train.columns) == ["col3"]
    assert list(supervised_data.y_test.columns) == ["col3"]


def test_supervised_data_invalid_input():
    # Test that an Exception is raised with invalid input

    toy_data = pd.DataFrame(
        {"col1": [1, 1, 1, 1], "col2": [2, 2, 2, 2], "col3": [3, 3, 3, 3]}
    )

    with pytest.raises(Exception):
        pymleda.SupervisedData(1, x_cols=["col1", "col2"], y_cols=["col3"])

    with pytest.raises(Exception):
        pymleda.SupervisedData(toy_data, x_cols=1, y_cols=["col3"])

    with pytest.raises(Exception):
        pymleda.SupervisedData(toy_data, x_cols=["col1", "col2"], y_cols=1)
