import typer
from .config import Plex
from enum import Enum

class Services(Enum):
    Plex = "plex"
    Telegram = "telegram"
    Matrix = "matrix"

app = typer.Typer()
plex = Plex()

@app.command()
def login(service: Services):
    """Log in to one of the services."""
    if service == Services.Plex:
        print("Plex")
        plex.login()


@app.callback()
def callback():
    """
    This application allows you to query your currently playing media
    and to send i as a sosial message to a friend
    on one of the supported platforms.
    """


@app.command()
def current_track():
    """
    This prints the current track that is being played.
    """
    typer.echo("Playing ...")
    typer.echo(plex.current_track())
