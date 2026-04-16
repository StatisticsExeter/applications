import click
import pandas as pd


@click.command()
@click.option('--template', type=click.Path(exists=True))
@click.option('--lda-csv', type=click.Path(exists=True))
@click.option('--qda-csv', type=click.Path(exists=True))
@click.option('--output', type=click.Path())
def main(template, lda_csv, qda_csv, output):
    with open(template, 'r') as f:
        content = f.read()
    df = pd.read_csv(lda_csv, index_col=0)
    df.index.name = "Metric"
    clean_df = df.reset_index()
    lda_md = clean_df.to_markdown(index=False, tablefmt="pipe")
    df_qda = pd.read_csv(qda_csv, index_col=0).round(2)
    qda_md = df_qda.to_markdown(index=False, tablefmt="pipe")
    content = content.replace('{{LDA_TABLE}}', lda_md)
    content = content.replace('{{QDA_TABLE}}', qda_md)
    with open(output, 'w') as f:
        f.write(content)
    click.echo(f"Report assembled at {output}")


if __name__ == '__main__':
    main()
