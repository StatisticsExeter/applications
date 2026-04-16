import click
import joblib
import pandas as pd
from pathlib import Path
import sys
# The next few lines ensure that the project root is in the Python path,
# allowing us to import modules from the project.
script_path = Path(__file__).resolve()
PROJECT_ROOT = script_path.parents[3]
if (str(PROJECT_ROOT) not in sys.path):
    sys.path.insert(0, str(PROJECT_ROOT))
from course.regression.regression_core import plot_caterpillar, plot_residuals  # noqa: E402


@click.command()
@click.option('--model-in', type=click.Path(exists=True), help="Path to .joblib model")
@click.option('--re-csv-in', type=click.Path(exists=True), help="Path to random effects CSV")
@click.option('--caterpillar-out', type=click.Path(), help="Save path for caterpillar plot")
@click.option('--resid-out', type=click.Path(), help="Save path for residual plot")
def main(model_in, re_csv_in, caterpillar_out, resid_out):

    results = joblib.load(model_in)
    re_df = pd.read_csv(re_csv_in)
    for out in [caterpillar_out, resid_out]:
        Path(out).parent.mkdir(parents=True, exist_ok=True)
    fig_cat = plot_caterpillar(re_df)
    fig_cat.savefig(caterpillar_out)
    fig_res = plot_residuals(results)
    fig_res.savefig(resid_out)
    click.echo("Regression diagnostics and plots generated.")


if __name__ == "__main__":
    main()
