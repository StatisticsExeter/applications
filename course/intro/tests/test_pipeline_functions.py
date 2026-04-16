import pytest
import pandas as pd
import matplotlib.pyplot as plt
from ..pipeline_functions import (
    tyler_viglen, calculate_correlation, filter_data, fit_regression, plot_scatter)


def test_tyler_viglen():
    df = tyler_viglen()
    assert len(df) == 23
    assert isinstance(df, pd.DataFrame)


def test_filter_data():
    df = pd.DataFrame({
        'Year': [2010, 2012, 2015, 2018],
        'Value': [1, 2, 3, 4]
    })
    filtered = filter_data(df, 2015)
    assert all(filtered['Year'] < 2015)
    assert len(filtered) == 2


def test_filter_data_is_strictly_less_than():
    # Setup test data
    data = pd.DataFrame({
        'Year': [2018, 2019, 2020, 2021, 2022],
        'Value': [10, 20, 30, 40, 50]
    })
    cutoff = 2021
    result = filter_data(data, cutoff)
    # 1. Check if the result is a DataFrame
    assert isinstance(result, pd.DataFrame), "The function must return a DataFrame."
    # 2. Check that years equal to or greater than the cutoff are removed
    # 2021 should NOT be in the result
    assert 2021 not in result['Year'].values, "The filter should be strictly less than (not <=)."
    assert 2022 not in result['Year'].values
    # 3. Check that the correct years remain
    expected_years = [2018, 2019, 2020]
    assert list(result['Year']) == expected_years, \
        f"Expected {expected_years}, but got {list(result['Year'])}"


def test_filter_data_empty_result():
    # Check behavior when no rows meet the criteria
    data = pd.DataFrame({'Year': [2025, 2026]})
    result = filter_data(data, 2000)
    assert len(result) == 0, "The result should be an empty DataFrame if no rows match."


@pytest.mark.parametrize("input_df, expected_r", [
    (pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [2, 4, 6, 8, 10]
    }), 1),
])
def test_calculate_correlation_basic(input_df, expected_r):
    corr, p = calculate_correlation(input_df, 'x', 'y')
    assert round(corr, 2) == expected_r


def test_fit_regression_basic():
    df = pd.DataFrame({
        'x': [1, 2, 3, 4, 5],
        'y': [2, 4, 6, 8, 10]
    })
    model = fit_regression(df, 'x', 'y')
    assert round(model.params['x'], 2) == 2.0
    assert round(model.rsquared, 2) == 1.0


def test_fit_regression_model_type():
    df = pd.DataFrame({
        'x': [1, 2, 3],
        'y': [2, 4, 6]
    })
    model = fit_regression(df, 'x', 'y')
    assert hasattr(model, 'params')
    assert hasattr(model, 'rsquared')


def test_plot_scatter_returns_correct_type():
    # Create dummy data
    data = pd.DataFrame({
        'kerosene': [1, 2, 3],
        'divorce_rate': [4, 5, 6]
    })
    # Call the function
    result = plot_scatter(data, 'kerosene', 'divorce_rate')
    # Check if the result is the matplotlib.pyplot module
    # (Since the function returns 'plt')
    assert result.__name__ == 'matplotlib.pyplot'
    # Further check: Does the current figure have data?
    ax = plt.gca()
    assert len(ax.collections) > 0, "The scatter plot should contain a PathCollection (the dots)."
    # Clean up to avoid memory leaks/cross-test interference
    plt.close('all')
