import click
import subprocess
from pathlib import Path


@click.command()
@click.option("--template-md", type=click.Path(exists=True))
@click.option("--summary-txt", type=click.Path(exists=True))
@click.option("--output-html", type=click.Path())
def main(template_md, summary_txt, output_html):
    click.echo("Starting report generation...")
    # Read the template and the text summary
    content = Path(template_md).read_text()
    summary_data = Path(summary_txt).read_text()
    # Inject the summary into the Markdown
    final_md = content.replace("{{summary_table}}", summary_data)
    # Write temp file and call Pandoc
    temp_md = Path("temp_report.md")
    temp_md.write_text(final_md)
    subprocess.run([
        "pandoc", str(temp_md),
        "-o", output_html,
        "--self-contained",
        "--resource-path=."
    ], check=True)
    temp_md.unlink()
    click.echo("Report rendered via Pandoc.")


if __name__ == "__main__":
    main()
