from sklearn.model_selection import train_test_split

class SupervisedData:
    """A wrapper class for simplifying data splitting

    Wrapper that utilizes `sklearn.model_selection.train_test_split` to perform data spltting 
    and provides convenient access to `X` and `y` portions of both the test split and the train split.

    Parameters
    ----------
    data : pandas dataframe
        Data set to be used for splitting
    
    x_cols: *array
        Sequence of feature names (X) to be used as independent variables 

    y_cols: *array
        Sequence of target names (y) to be used as dependent variables or labels

    **kawrgs: 
        Additional parameters to pass to sklearn's train_test_split(). For more information see hyperlink: `sklearn's function documentation <https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html/>`_.
    
    Attributes
    ----------
    data : pandas dataframe
        The original data set

    train_df: pandas dataframe
        The training portion of the dataset
    
    test_df: pandas dataframe
        The test portion of the dataset

    x_train : pandas dataframe
        The training portion of the dataset containing `X` features only.

    y_train: pandas dataframe
        The training portion of the dataset containing `y` targets only.

    x_test: pandas dataframe
        The test portion of the dataset containing `X` features only.

    y_test: pandas dataframe
        The test portion of the dataset containing `y` targets only.
    """

    def __init__(self, data, x_cols, y_cols, **kwargs):

