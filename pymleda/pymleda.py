import pandas as pd
from sklearn.model_selection import train_test_split


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
    Identify and impute missing values in a dataframe.
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
    return imputed_df


def dfscaling(df):
    """
    Apply standard scaling to the numeric features of a given dataframe.
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
    return scaled_df
