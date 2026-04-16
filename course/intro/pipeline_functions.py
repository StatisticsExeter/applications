import numpy as np
import pandas as pd
from scipy.stats import pearsonr
import statsmodels.api as sm
import matplotlib.pyplot as plt


def plot_scatter(df, x_name, y_name):
    """
    Create and return a styled scatter plot using Matplotlib.

    Instructions:
    1. Initialize a new figure with a width of 8 inches and a height of 6 inches.
    2. Create a scatter plot using the columns specified by 'x_name' and 'y_name'
       from the provided DataFrame 'df'.
    3. Set the point color to 'teal' and the transparency (alpha) to 0.7.
    4. Add the following labels:
       - Title: 'Spurious Correlation: Kerosene vs Divorce Rate'
       - X-axis: 'Kerosene (consumption)'
       - Y-axis: 'Divorce Rate (per 1000)'
    5. Enable the grid with a dashed ('--') linestyle and an alpha of 0.6.
    6. Return the matplotlib.pyplot module object.

    Parameters:
    df (pd.DataFrame): The dataset containing the variables.
    x_name (str): The column name for the x-axis.
    y_name (str): The column name for the y-axis.

    Returns:
    matplotlib.pyplot: The pyplot module after the figure has been generated.
    """
    pass


def calculate_correlation(df, x1, x2):
    """
    Calculate the Pearson correlation coefficient and its p-value for two variables.

    Instructions:
    1. Utilize the 'pearsonr' function from the 'scipy.stats' library.
    2. Extract the data for the two variables using the column names provided in
       the 'x1' and 'x2' arguments from the DataFrame 'df'.
    3. The function must return a tuple containing two floats:
       - The first value should be the Pearson correlation coefficient (r).
       - The second value should be the p-value (significance).

    Parameters:
    df (pd.DataFrame): The DataFrame containing the data.
    x1 (str): The name of the first column.
    x2 (str): The name of the second column.

    Returns:
    tuple: (correlation_coefficient, p_value)
    """
    pass


def fit_regression(df, x_name, y_name):
    """
    Fit an Ordinary Least Squares (OLS) regression model using statsmodels.

    Instructions for the student:
    1. Import the 'statsmodels.api' library (typically as 'sm').
    2. Define the dependent variable (Y) using the column 'y_name' and the
       independent variable (X) using the column 'x_name'.
    3. Crucial: Manually add a constant (intercept term) to the X variable
       using the 'add_constant' utility from statsmodels.
    4. Initialize the OLS model with the dependent variable (Y) and the
       augmented independent variable (X).
    5. Fit the model and return the resulting 'RegressionResultsWrapper' object.

    Parameters:
    df (pd.DataFrame): The dataset containing the variables.
    x_name (str): The column name for the independent variable (predictor).
    y_name (str): The column name for the dependent variable (target).

    Returns:
    statsmodels.regression.linear_model.RegressionResultsWrapper: The fitted model.
    """
    pass


def filter_data(df, year):
    """
    Filter the DataFrame to include only records from years prior to a given threshold.

    Instructions for the student:
    1. Identify the column named 'Year' within the input DataFrame 'df'.
    2. Apply a filter to select rows where the 'Year' value is strictly less than
       the integer provided in the 'year' argument.
    3. Ensure the function returns a new DataFrame (or a view) containing only
       these filtered rows.
    4. Do not include rows where the year is equal to the supplied 'year' value.

    Parameters:
    df (pd.DataFrame): The dataset containing a 'Year' column.
    year (int): The cutoff year (exclusive).

    Returns:
    pd.DataFrame: A filtered version of the input DataFrame.
    """
    pass


def tyler_viglen():
    """Create the data used at
    https://www.tylervigen.com/
    spurious/correlation/19524_kerosene-used-in-india_correlates-with_the-divorce-rate-in-maine"""
    array_1 = np.array([
      227, 238.806, 220.93, 220.358, 216.652, 198.424, 198.587, 201.298,
      198.333, 196.481, 197.041, 189.078, 183, 166, 157, 154, 149, 128,
      88, 76.9508, 59.2101, 40.4265, 34.1946
      ])
    array_2 = np.array([
      5.1, 5, 4.7, 4.6, 4.4, 4.3, 4.1, 4.2, 4.2, 4.2, 4.1, 4.2, 4.2, 3.9,
      3.96973, 3.58172, 3.42805, 3.42852, 3.22627, 3.19709, 3.033, 2.40567, 2.72837
      ])
    years = np.arange(1999, 2022)
    return pd.DataFrame({'Year': years, 'Kerosene': array_1, 'DivorceRate': array_2})
