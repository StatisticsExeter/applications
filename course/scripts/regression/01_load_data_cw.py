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
from course.utils import load_pg_data  # noqa: E402


@click.command()
@click.option("--sql-file", type=click.Path(exists=True))
@click.option("--outfile", type=click.Path())
def main(sql_file, outfile):
    p = Path(outfile)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(sql_file, 'r') as file:
        QUERY = file.read()
        df = load_pg_data(QUERY)
    df.to_csv(p, index=False)
    print(df.head())


if __name__ == "__main__":
    main()
