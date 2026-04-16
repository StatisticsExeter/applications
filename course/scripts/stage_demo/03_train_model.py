import click
import pandas as pd
# The next few lines ensure that the project root is in the Python path,
# allowing us to import modules from the project.
import sys
from pathlib import Path
script_path = Path(__file__).resolve()
PROJECT_ROOT = script_path.parents[3]
if (str(PROJECT_ROOT) not in sys.path):
    sys.path.insert(0, str(PROJECT_ROOT))
# Now we can import any project-specific utilities if needed
from course.unsupervised_classification.unsupervised_core import (  # noqa: E402
    run_kmeans, scale_data, compute_linkage, create_dendrogram,
    plot_cluster_scatter, project_pca, plot_centroids)


@click.command()
@click.option("--input-csv", type=click.Path(exists=True), required=True)
@click.option("--out-dir", type=click.Path(), required=True)
def main(input_csv, out_dir):
    df = pd.read_csv(input_csv)
    p = Path(out_dir)
    scaler, df_scaled = scale_data(df)
    Z = compute_linkage(df_scaled)
    fig_dendro = create_dendrogram(Z, title="Dendrogram")
    fig_dendro.savefig(p / "dendrogram.jpg", format='jpg', dpi=150)
    click.echo(f"Dendrogram saved in {p}")
    model = run_kmeans(df_scaled, 3)
    df_pca = project_pca(df_scaled, 2)
    df_pca['cluster'] = model.labels_.astype(str)
    fig_scatter = plot_cluster_scatter(df_pca, model.labels_, "Clusters in PCA Space")
    figs = plot_centroids(model.cluster_centers_, scaler, df_scaled.columns, 3)
    figs[0].savefig(p / "kmeans_1.jpg", dpi=150)
    figs[1].savefig(p / "kmeans_2.jpg", dpi=150)
    fig_scatter.savefig(p / "kmeans_scatter.jpg", dpi=150)
    click.echo(f"K-means centroid plots saved in {out_dir}")


if __name__ == "__main__":
    main()
