import matplotlib.pyplot as plt
import seaborn as sns


def box_plot(df, cat_var, cont_var):
    """
    Instructions:
    Create a box plot showing the distribution of 'cont_var' for each 'cat_var'.
    Return the Matplotlib Axes object.
    """
    pass

def scatterplot_groups(df, xvar, yvar, groups):
    """
    Instructions:
    Create a scatter plot of xvar vs yvar, colored by 'groups'.
    Return the Matplotlib Axes object.
    """
    pass


def bar_chart_means(df, cat_var, continuous_var):
    """
    Instructions:
    1. Group by 'cat_var' and calculate the mean of 'continuous_var'.
    2. Create a bar plot of these means.
    3. Return the Matplotlib Axes object.
    """
    # Using Pandas built-in matplotlib wrapper
    pass


def stacked_bar_counts(df, cat_var_1, cat_var_2):
    """
    Instructions:
    1. Group the data by both categorical variables and count the sizes.
    2. Unstack the second categorical variable to prepare for plotting.
    3. Plot as a bar chart with 'stacked=True'.
    4. Return the Axes object.
    """
    pass


def scatterplot_matrix(df, numeric_cols):
    """
    Instructions:
    1. Use Seaborn's pairplot function to create a matrix of scatterplots.
    2. Use only the columns specified in 'numeric_cols'.
    3. Return the PairGrid object.
    """
    pass
