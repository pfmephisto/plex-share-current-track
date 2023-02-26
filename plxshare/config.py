import os
import shelve
from plexapi.myplex import MyPlexAccount, MyPlexPinLogin
from plexapi.server import PlexServer
from typing import Union
 # from functools import partial

CONFIG_PATH = full_path = os.path.expanduser("~/.config/plxshare.conf")


class Plex():

    def __init__(self):
        self.account = self._get_account()

        if not self.account:
            print("Please log in first")

    def login(self):
        print("Go to https://plex.tv/link to log")
        account = MyPlexPinLogin()
        print(f"And type {account.pin}")
        account.run(self._pin_login_callback)


    def current_track(self) -> str:

        if self.account:

            for resource in self.account.resources():

                if "server" in resource.provides.split(","):
                    server =  resource.connect()
                    sessions = server.sessions()

                    for session in sessions:

                        if session.TYPE == "track":
                            name = session.title
                            album = session.album().title
                            artist = session.artist().title

                            return f"Name: {name}\nAlbum: {album}\nArtist: {artist}"


    def _pin_login_callback(self, token: Union[None, str]):
#        account = MyPlexAccount(token=token)
#        username = account.username
        self._set_credentials(token=token)

    def _get_account(self) -> Union[None, MyPlexAccount]:

        if not  os.path.exists(CONFIG_PATH):
            return None

        with  shelve.open(CONFIG_PATH) as db:
            if not "PLEX_TOKEN" in db.keys():
               return None

            token = db["PLEX_TOKEN"]
            return MyPlexAccount(token)

    def _set_credentials(self, token: str):
        with  shelve.open(CONFIF_PATH) as db:
            db["PLEX_TOKEN"] = token

