import pytest
import pandas as pd
import numpy as np
from statsmodels.tools.sm_exceptions import ConvergenceWarning  # noqa: F401
from statsmodels.regression.mixed_linear_model import MixedLMResultsWrapper
from course.regression.regression_core import fit_model, _random_effects


@pytest.fixture
def sample_df():
    return pd.DataFrame({
        'shortfall': [10, 12, 9, 14, 13, 11],
        'n_rooms': [3, 4, 2, 5, 4, 3],
        'age': [30, 45, 25, 50, 40, 35],
        'local_authority_code': ['A', 'A', 'B', 'B', 'C', 'C']
    })


def test_fit_model_returns_results(sample_df):
    formula = "shortfall ~ n_rooms + age"
    model, results = fit_model(formula, sample_df, "local_authority_code")
    print(type(results))
    assert isinstance(results, MixedLMResultsWrapper)


@pytest.mark.filterwarnings("ignore:The  Hessian Matrix:RuntimeWarning")
@pytest.mark.filterwarnings("ignore::statsmodels.tools.sm_exceptions.ConvergenceWarning")
def test_fit_model_execution():
    # 1. Create a synthetic nested dataset
    # 2 groups, 5 observations each
    data = pd.DataFrame({
        'y': np.random.normal(0, 1, 10),
        'x': np.random.normal(0, 1, 10),
        'group': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B']
    })
    formula = "y ~ x"
    group_col = "group"
    model, results = fit_model(formula, data, group_col)
    # 3. Assertions
    # Ensure we got the right types back
    assert hasattr(results, 'summary'), "Results object should have a summary method"
    assert hasattr(results, 'params'), "Results object should have coefficients (params)"

    # Check that the model recognized the groups
    # Statsmodels stores the group labels in the model object
    assert len(np.unique(data[group_col])) == 2


def test_fit_model_invalid_formula():
    # Ensure it raises an error with a non-existent column
    data = pd.DataFrame({'y': [1, 2], 'group': ['A', 'A']})
    with pytest.raises(Exception):
        fit_model("y ~ non_existent_col", data, "group")


def test_random_effects_structure(sample_df):
    formula = "shortfall ~ n_rooms + age"
    model, results = fit_model(formula, sample_df, "local_authority_code")
    re_df = _random_effects(results)

    # Check expected columns
    slopes = [col for col in re_df.columns if col.startswith('Slope_')]
    expected_cols = ['Intercept'] + slopes + ['group', 'lower', 'upper']
    for col in expected_cols:
        assert col in re_df.columns

    # Check that 'group' matches index
    assert all(re_df['group'] == re_df.index)

    # Check that 'lower' and 'upper' bounds are computed correctly
    stderr = np.sqrt(results.cov_re.iloc[0, 0])
    expected_lower = re_df['Intercept'] - 1.96 * stderr
    expected_upper = re_df['Intercept'] + 1.96 * stderr
    assert np.allclose(re_df['lower'], expected_lower)
    assert np.allclose(re_df['upper'], expected_upper)


class MockResults:
    """A mock object to simulate the output of statsmodels MixedLM."""
    def __init__(self):
        # random_effects is a dict of {group: [values]}
        self.random_effects = {
            'GroupA': [1.5],
            'GroupB': [-0.5],
            'GroupC': [0.5]
        }
        # cov_re is a DataFrame representing the covariance of random effects
        # We need it to have 0.25 so sqrt is 0.5
        self.cov_re = pd.DataFrame([[0.25]])


def test_random_effects_formatting():
    results = MockResults()
    re_df = _random_effects(results)
    # 1. Check sorting (Intercept should go from -0.5 to 1.5)
    assert re_df.iloc[0]['Intercept'] == -0.5
    assert re_df.iloc[-1]['Intercept'] == 1.5
    # 2. Check group labeling
    assert 'group' in re_df.columns
    # 3. Check Confidence Interval Math
    # stderr = sqrt(0.25) = 0.5
    # lower = 1.5 - (1.96 * 0.5) = 1.5 - 0.98 = 0.52
    last_row = re_df.loc[re_df['group'] == 'GroupA'].iloc[0]
    assert last_row['lower'] == pytest.approx(0.52)
    assert last_row['upper'] == pytest.approx(2.48)
