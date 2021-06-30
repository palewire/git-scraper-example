import os
import click
import pathlib
from bln.client import Client

DATA_DIR = pathlib.Path(__file__).parent.parent / "data"


@click.command()
def main():
    """
    Archive the source data file.
    """
    token = os.getenv("BLN_TOKEN")
    c = Client(token)
    item_list = c.everything()['effectiveProjectRoles']
    project_name = "Iowa liquor stores"
    try:
        project = next(i['project'] for i in item_list if i['project']['name'] == project_name)
    except StopIteration:
        project = c.createProject(
            project_name,
            contact="b@palewi.re",
            isOpen=True,
        )
    c.upload_file(project['id'], DATA_DIR / "iowa-liquor-stores.csv")


if __name__ == '__main__':
    main()
