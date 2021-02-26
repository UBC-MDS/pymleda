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
