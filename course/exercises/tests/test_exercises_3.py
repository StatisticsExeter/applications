import pytest
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from course.exercises.exercises_3 import (
    box_plot, scatterplot_groups, scatterplot_matrix,
    bar_chart_means, stacked_bar_counts
)


def test_scatterplot_groups_logic():
    # Setup
    df = pd.DataFrame({
        'x': [1, 2, 3],
        'y': [4, 5, 6],
        'label': ['A', 'A', 'B']
    })
    ax = scatterplot_groups(df, 'x', 'y', 'label')
    # 1. Check if it's the right type
    assert isinstance(ax, plt.Axes)
    # 2. Check the labels
    assert ax.get_xlabel() == 'x'
    assert ax.get_ylabel() == 'y'
    # 3. Check if a legend was created (because we have groups)
    assert ax.get_legend() is not None
    plt.close()


def test_bar_chart_means_logic():
    # Setup dummy data
    df = pd.DataFrame({
        'Species': ['Adelie', 'Adelie', 'Gentoo'],
        'Mass': [3000, 3500, 5000]
    })
    # Run the function
    ax = bar_chart_means(df, 'Species', 'Mass')
    # 1. Verify it returns the correct Matplotlib type
    assert isinstance(ax, plt.Axes), "Function should return a Matplotlib Axes object."
    # 2. Check the Title
    expected_title = "Average Mass by Species"
    msg = f"Expected title '{expected_title}', got '{ax.get_title()}'"
    assert ax.get_title() == expected_title, msg
    # 3. Verify there are bars on the plot
    # Bars are stored as 'patches' in the Axes object
    bars = [p for p in ax.patches]
    assert len(bars) == 2, "Expected 2 bars (one for each species), but found a different amount."
    plt.close()


@pytest.mark.filterwarnings("ignore:vert. bool will be deprecated")
def test_box_plot_logic():
    # Setup dummy data
    df = pd.DataFrame({
        'Island': ['Biscoe', 'Biscoe', 'Dream', 'Dream'],
        'Length': [39.1, 39.5, 40.3, 36.7]
    })
    # Run the function
    ax = box_plot(df, 'Island', 'Length')
    # 1. Verify return type
    assert isinstance(ax, plt.Axes)
    # 2. Check labels (Seaborn/Matplotlib auto-assigns these from the df)
    assert ax.get_xlabel() == 'Island'
    assert ax.get_ylabel() == 'Length'
    # 3. Verify it is actually a box plot
    # In Seaborn/Matplotlib, box plots create 'PathCollections' or 'artists'
    # Checking for the lines (whiskers/fliers) or patches (the boxes)
    msg = "No plot elements found. Did you call the boxplot function?"
    assert len(ax.artists) + len(ax.lines) > 0, msg
    plt.close()


@pytest.mark.filterwarnings("ignore:vert. bool will be deprecated")
def test_box_plot_returns_axes():
    df = pd.DataFrame({'cat': ['A', 'B'], 'val': [1, 2]})
    ax = box_plot(df, 'cat', 'val')
    assert isinstance(ax, plt.Axes)
    assert ax.get_title() == "val by cat"
    # Check if a boxplot (Artist) was actually drawn
    assert len(ax.artists) > 0 or len(ax.patches) > 0


def test_scatterplot_matrix_logic():
    # Setup dummy data with 3 numeric columns
    df = pd.DataFrame({
        'bill_length': [39.1, 39.5, 40.3],
        'bill_depth': [18.7, 17.4, 18.0],
        'flipper_length': [181, 186, 195],
        'species': ['Adelie', 'Adelie', 'Adelie']
    })
    cols = ['bill_length', 'bill_depth', 'flipper_length']
    grid = scatterplot_matrix(df, cols)
    # 1. Verify it returns a Seaborn PairGrid
    assert isinstance(grid, sns.axisgrid.PairGrid), "Should return a Seaborn PairGrid object."
    # 2. Verify the grid dimensions (3x3 for 3 columns)
    # The axes attribute is a 2D array of the subplots
    assert grid.axes.shape == (3, 3), f"Expected 3x3 grid, got {grid.axes.shape}"
    # 3. Verify the super-title (centered at the top of the figure)
    # Note: suptitle can sometimes be None if not set correctly on the figure object
    assert "Penguin Features" in grid.fig._suptitle.get_text()
    plt.close('all')


def test_stacked_bar_counts_logic():
    # Setup data with two categories
    df = pd.DataFrame({
        'Island': ['Biscoe', 'Biscoe', 'Dream', 'Dream'],
        'Sex': ['MALE', 'FEMALE', 'MALE', 'MALE']
    })
    ax = stacked_bar_counts(df, 'Island', 'Sex')
    # 1. Verify return type
    assert isinstance(ax, plt.Axes)
    # 2. Check that a legend exists (to distinguish 'Sex')
    assert ax.get_legend() is not None, "Stacked bar should have a legend for the second category."
    # 3. Verify the "Stacked" property
    # In a stacked bar, multiple patches will have the same 'x' coordinate
    x_positions = [p.get_x() for p in ax.patches]
    unique_x = set(x_positions)
    msg = "Bars do not appear to be stacked (multiple bars should share x-positions)."
    assert len(x_positions) > len(unique_x), msg
    # 4. Check Title
    assert "Counts by Island and Sex" in ax.get_title()
    plt.close('all')
