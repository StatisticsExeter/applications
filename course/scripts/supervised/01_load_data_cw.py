import click
from pathlib import Path
import sys


# Ensure project root is on the Python path
script_path = Path(__file__).resolve()
PROJECT_ROOT = script_path.parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from course.utils import load_pg_data  # noqa: E402


COLUMNS_TO_KEEP = [
    "passenger_injured",
    "day_of_year",
    "hour_of_day",
    "speed_limit_mph",  # called speed_limit in 2025
    "engine_capacity_cc",
    "vehicle_age",
    "driver_age",
]


@click.command()
@click.option("--sql-file", type=click.Path(exists=True), required=True)
@click.option("--outfile", type=click.Path(), required=True)
def main(sql_file, outfile):
    """
    Load Stats19-derived data from Postgres, clean it,
    and write a modelling-ready CSV.
    """
    with open(sql_file, "r") as f:
        query = f.read()

    df = load_pg_data(query)
    df = df[COLUMNS_TO_KEEP]
    df_clean = (df.dropna().loc[~(df == -1).any(axis=1)].reset_index(drop=True))
    outpath = Path(outfile)
    outpath.parent.mkdir(parents=True, exist_ok=True)
    df_clean.to_csv(outfile, index=False)
    click.echo(f"Rows before cleaning: {len(df)}")
    click.echo(f"Rows after cleaning : {len(df_clean)}")
    click.echo("")
    click.echo(df_clean.head())


if __name__ == "__main__":
    main()
