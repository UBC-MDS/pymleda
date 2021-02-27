from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import pandas as pd
pd.DataFrame()

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
        Additional parameters to pass to sklearn's train_test_split(). For more information see hyperlink: `sklearn's function documentation <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html/>`_.
        In the absence of additional **kwargs parameters for `sklearn.model_selection.train_test_split`, the default paramteres of test size  = 0.25 is used
    
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
    >>> supervised_data = SupervisedData(data, x_cols = ['feature1', 'feature2'], y_cols = ['target'])
    
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
      The data frame contains summary value which comes from describe().
    unique : pandas.DataFrame
      The data frame contains unique entries and its length for non-numerical columns.   

    Examples
    --------
    >>> from pymleda import pymleda
    >>> df = pd.read_csv("test_data.csv")
    >>> pymleda.dftype(df)
    """

    return summary, unique
    

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