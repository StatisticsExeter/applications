import click
import subprocess
from pathlib import Path


@click.command()
@click.option('--template-md', type=click.Path(exists=True))
@click.option('--summary-txt', type=click.Path(exists=True))
@click.option('--output-html', type=click.Path())
def main(template_md, summary_txt, output_html):
    output_path = Path(output_html)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(summary_txt, 'r') as f:
        summary_content = f.read()
    with open(template_md, 'r') as f:
        report_content = f.read().replace('{{MODEL_SUMMARY}}', summary_content)
    temp_md = Path("temp_final_report.md")
    temp_md.write_text(report_content)
    try:
        subprocess.run([
            'pandoc',
            str(temp_md),
            '-o', str(output_path),
            '--to', 'html5',
            '--standalone',
            '--embed-resources',
            '--mathjax',
            '--metadata', 'title=Regression Coursework Report'
        ], check=True)
        click.echo(f"Successfully rendered report to {output_html}")
    except subprocess.CalledProcessError as e:
        click.echo(f"Pandoc failed: {e}")
    finally:
        if temp_md.exists():
            temp_md.unlink()


if __name__ == "__main__":
    main()
