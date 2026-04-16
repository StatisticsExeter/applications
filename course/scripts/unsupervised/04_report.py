import click
import subprocess
from pathlib import Path


@click.command()
@click.option("--input-md", type=click.Path(exists=True))
@click.option("--output-html", type=click.Path())
def main(input_md, output_html):
    Path(output_html).parent.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        "pandoc", input_md, "-o", output_html,
        "--self-contained", "--embed-resources", "--resource-path=."
    ], check=True)
    click.echo(f"Report rendered: {output_html}")


if __name__ == "__main__":
    main()
