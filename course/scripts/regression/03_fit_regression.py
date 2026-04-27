import click
import pandas as pd
from pathlib import Path
import sys
import joblib
import re
# The next few lines ensure that the project root is in the Python path,
# allowing us to import modules from the project.
script_path = Path(__file__).resolve()
PROJECT_ROOT = script_path.parents[3]
if (str(PROJECT_ROOT) not in sys.path):
    sys.path.insert(0, str(PROJECT_ROOT))
# Import your logic from the core module
from course.regression.regression_core import (  # noqa: E402
    fit_model, _random_effects, _save_model_summary)


@click.command()
@click.option('--input-csv', type=click.Path(exists=True), help="Path to cleaned data")
@click.option('--formula', type=str, help="Statsmodels formula")
@click.option('--group-col', type=str, help="Column for random effects")
@click.option('--summary-out', type=click.Path(), help="Path for text summary")
@click.option('--re-csv-out', type=click.Path(), help="Path for random effects CSV")
@click.option('--model-out', type=click.Path(), help="Path to save serialized model object")
def main(input_csv, formula, group_col, summary_out, re_csv_out, model_out):
    df = pd.read_csv(input_csv)
    input_rows = len(df)
    formula_vars = re.findall(r'\b\w+\b', formula)
    model_cols = list(set(formula_vars + [group_col]))
    df = df.dropna(subset=model_cols).copy()
    df[group_col] = df[group_col].astype(str)
    df = df.reset_index(drop=True)
    total_rows = len(df)
    num_groups = df[group_col].nunique()
    click.echo("--- Model Diagnostics ---")
    click.echo(f"Rows available before cleaning: {input_rows}")
    click.echo(f"Rows remaining after cleaning: {total_rows}")
    click.echo(f"Number of unique groups ({group_col}): {num_groups}")
    click.echo(f"Average rows per group: {total_rows / num_groups:.2f}")
    click.echo(f"Formula: {formula}")
    click.echo("-------------------------")
    model, results = fit_model(formula, df, group_col)
    for out in [summary_out, re_csv_out, model_out]:
        if out:
            Path(out).parent.mkdir(parents=True, exist_ok=True)
    summary_text = _save_model_summary(results)
    with open(summary_out, "w") as f:
        f.write(summary_text)
    re_df = _random_effects(results)
    re_df.to_csv(re_csv_out, index=False)
    joblib.dump(results, model_out)
    click.echo(f"Model fitted successfully using formula: {formula}")


if __name__ == "__main__":
    main()
