import click
import pathlib
import requests

DATA_DIR = pathlib.Path(__file__).parent.parent / "data"


@click.command()
def main():
    """
    Download the source data file.
    """
    url = "https://data.iowa.gov/api/views/ykb6-ywnd/rows.csv?accessType=DOWNLOAD"
    r = requests.get(url)
    with open(DATA_DIR / "iowa-liquor-stores.csv", 'w') as f:
        f.write(r.text)


if __name__ == '__main__':
    main()
