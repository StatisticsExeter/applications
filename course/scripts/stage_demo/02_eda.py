import click
# The next few lines ensure that the project root is in the Python path,
# allowing us to import modules from the project.
import sys
import pandas as pd
from pathlib import Path
script_path = Path(__file__).resolve()
PROJECT_ROOT = script_path.parents[3]
if (str(PROJECT_ROOT) not in sys.path):
    sys.path.insert(0, str(PROJECT_ROOT))
# Now we can import any project-specific utilities if needed
from course.unsupervised_classification.unsupervised_core import (  # noqa: E402
    get_summary_stats, create_boxplot, scale_data, _scatter)


@click.command()
@click.option("--input-csv", type=click.Path(exists=True), required=True)
@click.option("--output-dir", type=click.Path(), required=True)
def main(input_csv, output_dir):
    df = pd.read_csv(input_csv)
    out_path = Path(output_dir)
    out_path.mkdir(parents=True, exist_ok=True)

    stats_text = get_summary_stats(df)
    (out_path / "lab_olive_oil_summary.txt").write_text(stats_text)

    fig_raw = create_boxplot(df, title="Raw Olive Oil Variables")
    fig_raw.savefig(out_path / "lab_olive_oil_raw_boxplot.jpg", dpi=150)

    _, df_scaled = scale_data(df)
    fig_scaled = create_boxplot(df_scaled, title="Scaled Olive Oil Variables")
    fig_scaled.savefig(out_path / "lab_olive_oil_scaled_boxplot.jpg", dpi=150)

    fig_scatter = _scatter(df, title="Scatter Matrix of Continuous Variables")
    fig_scatter.savefig(out_path / "lab_olive_oil_scatterplot.jpg", format='jpg', dpi=150)

    click.echo(f"EDA artifacts saved to {output_dir}")


if __name__ == "__main__":
    main()
