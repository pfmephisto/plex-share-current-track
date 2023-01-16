import os
import shelve
from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer


CONFIF_PATH = "~/.config/plxshare.conf"


class Plex():

    def __init__(self):

        self.account = None
        self.server = PlexServer()

    def login(self):
        print("Call function to log in")

        
    def _get_accoutn(self) -> MyPlexAccount:

        with  shelve.open(CONFIF_PATH) as db:
            if "PLEX_USER" in db.keys():
                if "PLEX_TOKEN" in db.keys():
                    return MyPlexAccount(db["PLEX_USER"], db["PLEX_TOKEN"])
            
            if self.server != None:
                return self.server.myPlexAccount()
            else:
                print("Server is missing and no userdata have been stored")


    def _set_credentials(self, username: str, token: str):
        #if os.path.exists(CONFIF_PATH):
        with  shelve.open(CONFIF_PATH) as db:
            db["PLEX_USER"] = username
            db["PLEX_TOKEN"] = token

