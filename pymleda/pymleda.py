



















def dftype(df):
    """
    Explore the type of data frame variables and columns.

    Parameters
    ----------
    df : pandas.core.frame.DataFrame
      A pandas data frame.

    Returns
    -------
    summary : pandas.core.frame.DataFrame
      The data frame contains summary value which comes from describe().
    unique : pandas.core.frame.DataFrame
      The data frame contains unique entries and its length for non-numerical columns.   

    Examples
    --------
    >>> from pymleda import pymleda
    >>> df = pd.read_csv("test_data.csv")
    >>> pymleda.dftype(df)

    """