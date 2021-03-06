import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from collections.abc import Sequence


class SupervisedData:
    """A wrapper class for simplifying data splitting
    Wrapper that utilizes `sklearn.model_selection.train_test_split` to perform data spltting
    and provides convenient access to `X` and `y` portions of both the test split and the train split.
    Parameters
    ----------
    data : pandas.DataFrame
        Data set to be used for splitting
    x_cols: *array
        Sequence of feature names (X) to be used as independent variables
    y_cols: *array
        Sequence of target names (y) to be used as dependent variables or labels
    **kawrgs:
        Additional parameters to pass to sklearn's train_test_split().
        In the absence of additional parameters, the default parameters of train_test_split() are used including test size  = 0.25
        For more information see hyperlink: `sklearn's function documentation <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html/>`_.

    Attributes
    ----------
    data : pandas.DataFrame
        The original data set
    train_df: pandas.DataFrame
        The training portion of the dataset

    test_df: pandas.DataFrame
        The test portion of the dataset
    x_train : pandas.DataFrame
        The training portion of the dataset containing `X` features only.
    y_train: pandas.DataFrame
        The training portion of the dataset containing `y` targets only.
    x_test: pandas.DataFrame
        The test portion of the dataset containing `X` features only.
    y_test: pandas.DataFrame
        The test portion of the dataset containing `y` targets only.
    Examples
    --------
    >>> from pymleda import pymleda
    >>> from sklearn.model_selection import train_test_split
    >>> supervised_data = SupervisedData(df, x_cols = ['feature1', 'feature2'], y_cols = ['target'])

    The original dataset
    >>> supervised_data.data
        feature1  feature2  target
    0     0         0           n
    1     1         1           y
    2     2         2           y
    3     3         3           y
    >>> supervised_data.train_df
        feature1  feature2  target
    0     0         0           n
    1     1         1           y
    3     3         3           y
    >>> supervised_data.test_df
        feature1  feature2  target
    2     2         2           y
    >>> supervised_data.x_train
        feature1  feature2
    0     0         0
    1     1         1
    3     3         3
    >>> supervised_data.y_train
        target
    0   n
    1   y
    3   y
    >>> supervised_data.x_test
        feature1  feature2
    2     2         2
    >>> supervised_data.y_test
        target
    2   y
    """

    def __init__(self, data, x_cols, y_cols, **kwargs):
        """See help(SupervisedData)"""

        if not isinstance(data, pd.DataFrame):
            raise Exception("TypeError: data must be a pandas dataframe")
        if not isinstance(x_cols, Sequence):
            raise Exception("TypeError: x_cols must be a sequence of columns")
        if not isinstance(y_cols, Sequence):
            raise Exception("TypeError: y_cols must be a sequence of columns")

        # Cast any sequence type to list so it can be used for indexing a pandas df
        x_cols = list(x_cols)
        y_cols = list(y_cols)

        self.data = data
        self.train_df, self.test_df = train_test_split(data, **kwargs)

        self.x_train = self.train_df[x_cols]
        self.y_train = self.train_df[y_cols]

        self.x_test = self.test_df[x_cols]
        self.y_test = self.test_df[y_cols]


def dftype(df):
    """
    Explore the type of data frame variables and columns.
    Parameters
    ----------
    df : pandas.DataFrame
      A pandas data frame.
    Returns
    -------
    summary : pandas.DataFrame
      The data frame contains summary numeric values which come from describe().
    unique_val : pandas.DataFrame
      The data frame contains unique entries and their length in case of non-numerical columns.

    Examples
    --------
    >>> from pymleda import pymleda
    >>> df = pd.DataFrame({
    >>>     'type':['Air','Ship','Bus', 'Air' ],
    >>>     'time':[6,32,31,5],
    >>>     'origin': ['US', 'Mexico', 'CANADA', 'UK']
    >>>      })
    >>> summary, unique_df = pymleda.dftype(df)
    """

    summary = df.describe()

    cols = df.columns
    num_cols = df._get_numeric_data().columns
    non_num_cols = list(set(cols) - set(num_cols))

    unique = {"column_name": [], "unique_values": [], "num_unique_values": []}

    for cat in non_num_cols:
        unique["column_name"].append(cat)
        unique["unique_values"].append(df[cat].unique())
        unique["num_unique_values"].append(len(df[cat].unique()))

    unique_val = pd.DataFrame(unique)

    return summary, unique_val


def autoimpute_na(df):
    """
    Identify and impute missing values with the mean for numeric columns and the most frequent value for categorical columns in a dataframe.
    Parameters
    ----------
    df : pandas.DataFrame
        A pandas dataframe.
    Returns
    -------
    pandas.DataFrame
        A pandas dataframe with imputed missing values.
    Examples
    --------
    >>> from pymleda import pymleda
    >>> pymleda.autoimpute_na(toy_df)
    """

    if not isinstance(df, pd.DataFrame):
        raise Exception("TypeError: df must be a pandas dataframe.")

    # Check if there are any missing values entered manually
    rogue_na = [
        "na",
        "n/a",
        "n\a",
        "nan",
        "NAN",
        "NA",
        "N/A",
        "N\\A",
        "not available",
        "Not available",
        "-",
        "--",
        "---",
    ]
    df.replace(rogue_na, np.nan, inplace=True)
    # Replace entered manually missing values with NaN

    # If there are no missing values, then return the original df
    col_count = 0
    for col in df:
        if np.sum(df[col].isnull()) == 0:
            col_count += 1
            if col_count == len(df.columns):
                imputed_df = df
                print(
                    "There are no missing values in the dataframe! I am returning the original dataframe!"
                )

    numeric_columns = df.select_dtypes(include=["number"]).columns.values
    categorical_columns = df.select_dtypes(exclude=["number", "bool_"]).columns.values
    for col in df:
        if np.sum(df[col].isnull()) > 0:
            for (
                col
            ) in (
                numeric_columns
            ):  # Fill missing values with the mean for numeric columns
                if np.sum(df[col].isnull()) > 0:
                    print("Missing values were imputed in the", (col), "column.")
                    df[col] = df[col].fillna(df[col].mean())
            for (
                col
            ) in (
                categorical_columns
            ):  # Fill missing values with the most frequent value for categorical columns
                if np.sum(df[col].isnull()) > 0:
                    print("Missing values were imputed in the", (col), "column.")
                    df[col] = df[col].fillna(df[col].describe()["top"])
    imputed_df = df

    return imputed_df


def dfscaling(df):
    """
    Apply standard scaling and centering to the numeric features of a given dataframe.
    The standard score of a sample x is calculated as:
      z = (x - u) / s
    where u is the mean of the training samples, and s is the standard deviation of the training samples.
    Parameters
    ----------
    df : pandas.DataFrame
        A pandas data frame.
    Returns
    -------
    scaled_df : pandas.DataFrame
      A data frame with standard scaling applied to the numeric features.

    Examples
    --------
    >>> from pymleda import pymleda
    >>> df = pd.read_csv("test_data.csv")
    >>> dfscaling(df)
    """
    if not isinstance(df, pd.DataFrame):
        raise Exception("TypeError: df must be a pandas dataframe.")

    assert len(list(df.select_dtypes(include=[np.number]))) != (
        0
    ), "There should be at least one numeric column in the input dataframe."
    # select numeric features in the dataframe
    numeric_features = list(df.select_dtypes(include=[np.number]))
    # select only the numeric features for centering and scaling
    scaled_df = df[numeric_features]

    # Fit and transform the dataframe
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(scaled_df.values)
    scaled_df = pd.DataFrame(
        scaled_features, index=scaled_df.index, columns=scaled_df.columns
    )

    return scaled_df
