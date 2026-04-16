import click
from pathlib import Path
import sys
# The next few lines ensure that the project root is in the Python path,
# allowing us to import modules from the project.
script_path = Path(__file__).resolve()
PROJECT_ROOT = script_path.parents[3]
if (str(PROJECT_ROOT) not in sys.path):
    sys.path.insert(0, str(PROJECT_ROOT))
# Now we can import any project-specific utilities if needed
from course.utils import prepare_collision_data  # noqa: E402


@click.command()
@click.option("--sql-file", type=click.Path(exists=True))
@click.option("--output-csv", type=click.Path())
def main(sql_file, output_csv):
    query = Path(sql_file).read_text()
    df_eda, df = prepare_collision_data(query)
    Path(output_csv).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_csv, index=False)
    click.echo(f"Data saved to {output_csv}")


if __name__ == "__main__":
    main()
