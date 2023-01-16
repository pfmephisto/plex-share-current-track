import typer
from .config import Plex
from enum import Enum

class Services(Enum):
    Plex = "plex"

app = typer.Typer()
plex = Plex()

@app.command()
def login(service: Services):

    if service == Services.Plex:
        print("Plex")
        plex.login()


@app.callback()
def callback():
    """
    Awesome Portal Gun
    """


@app.command()
def shoot():
    """
    Shoot the portal gun
    """
    typer.echo("Shooting portal gun")


@app.command()
def load():
    """
    Load the portal gun
    """
    typer.echo("Loading portal gun")


@app.command()
def shootme(name:str):
    print(f'{name} has been shot')