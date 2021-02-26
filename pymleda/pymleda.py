from sklearn.model_selection import train_test_split

class SupervisedData:
    """A wrapper class for simplifying data splitting

    Wrapper that utilizes `sklearn.model_selection.train_test_split` to perform data spltting 
    and provides convient access to X and y portions of both the test and the train splits.

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
    """

    def __init__(self, data, x_cols, y_cols, **kwargs):

