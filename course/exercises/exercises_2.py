def column_mean(df, column):
    """
    Given a data frame 'df' and a column name 'column'
    return the mean of the specified column.
    """
    pass


def select_row(df, x):
    """
    Instructions:
    Return the x-th row of the DataFrame.
    Ensure the result is returned as a Series object (using single-bracket iloc).
    """
    pass


def frequencies_by_group(df, cat_col):
    """
    Given a dataframe 'df' and the name of a categorical
    variable column 'cat_col'
    return frequency counts of that categorical column as a Series.
    """
    pass


def filter_rows(df, column, threshold):
    """
    Given a dataframe 'df', the name of a column 'column'
    and a float indicating a threshold 'threshold'
    return rows where the column value is greater than the threshold.
    """
    pass


def add_ratio_column(df, numerator, denominator, new_col):
    """
    Instructions:
    1. Calculate the ratio of the 'numerator' column to the 'denominator' column.
    2. Add this as a new column named 'new_col'.
    3. Return a NEW DataFrame containing this column without modifying the original.
    """
    pass


def rename_columns(df, columns_dict):
    """
    Given a dataframe 'df# and a dictionary that maps
    existing column names to new names, return a dataframe
    with the new names.
    """
    pass


def drop_missing(df):
    """
    Given a dataframe 'df'
    return a dataframe having dropped rows with any
    missing values.
    """
    pass


def fill_missing(df, value):
    """
    Given a dataframe 'df' and a marker for missing values 'value'
    (which could be NA)
    return a data frame where the missing values with this specified value.
    """
    pass


def sort_by_column(df, column, ascending=True):
    """
    Given the dataframe 'df' and the name of a column 'column'
    return a DataFrame sorted by that specified column.
    """
    pass


def unique_values(df, column):
    """
    Given a dataframe 'df' and a named column 'column'
    return unique values as a Numpy array from that specified column.
    """
    pass
