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

    # Check if there are any missing values entered manually
    rogue_na = ['na', 'n/a', 'n\a', 'NA', 'N/A', 'N\A', 'not available', 'Not available', '-', '--', '---']
    df.replace(rogue_na, np.nan, inplace=True); # Replace entered manually missing values with NaN

    # If there are no missing values, then return the original df
    col_count = 0
    for col in df:
        if np.sum(df[col].isnull()) == 0:
            col_count += 1
            if col_count == len(df.columns):
                imputed_df = df
                print("There are no missing values in the dataframe! I am returning the original dataframe!")

    
    numeric_columns = df.select_dtypes(include=["number"]).columns.values
    categorical_columns = df.select_dtypes(exclude=["number", "bool_"]).columns.values
    for col in df:
        if np.sum(df[col].isnull()) > 0:
            for col in numeric_columns:            # Fill missing values with the mean for numeric columns
                if np.sum(df[col].isnull()) > 0:
                    print('Missing values were imputed in the', (col), 'column.')
                    df[col] = df[col].fillna(df[col].mean())
            for col in categorical_columns:        # Fill missing values with the most frequent value for categorical columns
                if np.sum(df[col].isnull()) > 0:
                    print('Missing values were imputed in the', (col), 'column.')
                    df[col] = df[col].fillna(df[col].describe()['top'])
    imputed_df = df

    return imputed_df