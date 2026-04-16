from pathlib import Path
from dotenv import load_dotenv
import os
import psycopg2
import pandas as pd
import sys
import textwrap
#from doit.exceptions import TaskFailed


def warn_if_in_rstudio():
    """Detect if running under RStudio/reticulate and print a warning."""
    # reticulate embeds Python in-process and sets these environment variables
    in_rstudio = any(
        "RSTUDIO" in k or "RETICULATE" in k for k in os.environ.keys()
    )

    if in_rstudio:
        msg = textwrap.dedent(f"""
        WARNING: This script appears to be running inside RStudio (reticulate).
        RStudio embeds Python in the R process, which can cause segfaults with
        libraries like psycopg2 and NumPy.

        Please re-run this script from a clean Anaconda prompt instead:
          conda activate python-exercises
          python {os.path.basename(sys.argv[0])}
        """)
        print(msg, file=sys.stderr)


# def check_input_file(path, hint=None):
#     """Return a TaskFailed object (not raise it) if the input file is missing."""
#     if not os.path.exists(path):
#         msg = f"Missing required input file: {path}"
#         if hint:
#             msg += f"\n Hint: {hint}"
#         # Return TaskFailed so doit interprets it as a controlled failure
#         print(msg, file=sys.stderr, flush=True)
#         return TaskFailed(msg)
#     return True


def load_pg_data(query):
    config = load_db_config()
    with get_db_connection(config) as conn:
        df = fetch_pg_data(conn, query)
    return df


def find_project_root(marker=".git"):
    """
    Traverse upward from the current file to find the project root.
    Includes the current file's directory in the search.
    """
    current_dir = Path.cwd().resolve()
    for directory in [current_dir] + list(current_dir.parents):
        if (directory / marker).exists():
            return directory
    raise RuntimeError("Project root not found. Please ensure a marker file exists.")


def load_db_config(env_path=None):
    if env_path is None:
        env_path = find_project_root()
    load_dotenv(dotenv_path=env_path / ".Renviron", override=True)
    return {
        "dbname": os.getenv("PGRDATABASE"),
        "user": os.getenv("PGRUSER"),
        "password": os.getenv("PGRPASSWORD"),
        "host": os.getenv("PGRHOST"),
        "port": os.getenv("PGRPORT"),
    }


def get_db_connection(config):
    return psycopg2.connect(**config)


def fetch_pg_data(conn, query):
    with conn.cursor() as cur:
        cur.execute(query)
        rows = cur.fetchall()
        colnames = [desc[0] for desc in cur.description]
    return pd.DataFrame(rows, columns=colnames)


def prepare_collision_data(query_text):
    """
    Instructions:
    1. Load raw data from PostgreSQL using the provided query.
    2. Set the 'local_authority_ons_district' column as the DataFrame index.
    3. Convert the denominator (column 0) and numerator columns (columns 1-6) 
       to float to ensure precise division.
    4. Normalize the numerator columns by dividing them by the denominator column 
       (the 'total' or 'population' value).
    5. Return the processed DataFrame containing the normalized rates.

    Parameters:
    query_text (str): SQL query to fetch raw collision and population data.

    Returns:
    pd.DataFrame: A DataFrame where columns 1-6 represent normalized rates.
    """
    df = load_pg_data(query_text)
    df.set_index("local_authority_ons_district", inplace=True)
    # Convert and normalize
    df[df.columns[1:7]] = df[df.columns[1:7]].astype(float)
    df[df.columns[0]] = df[df.columns[0]].astype(float)
    df.iloc[:, 1:7] = df.iloc[:, 1:7].div(df.iloc[:, 0], axis=0)
    df_clustering = df.iloc[:, 1:]
    return df, df_clustering
