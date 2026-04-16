import pandas as pd
import click
from pathlib import Path


@click.command()
@click.option("--input-csv", type=click.Path(exists=True), required=True)
@click.option("--processed-csv", type=click.Path(), required=True)
def main(input_csv, processed_csv):
    """Load and preprocess data."""
    df = pd.read_csv(input_csv)
    Path(processed_csv).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(processed_csv, index=False)
    click.echo(f"Processed data saved to {processed_csv}")


if __name__ == "__main__":
    main()
