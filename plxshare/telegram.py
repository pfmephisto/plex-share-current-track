import os
from telethon import TelegramClient

from dotenv import load_dotenv

load_dotenv()

CONFIG_PATH = os.path.expanduser("~/.config/plexshare/telegram")

class Telegram():

    def __init__(self):
        api_hash = os.environ['TELEGRAM_APP_HASH']
        api_id = os.environ['TELEGRAM_APP_ID']
        self.client = TelegramClient(CONFIG_PATH, api_id, api_hash)


    def login(self):
        if not self.client.is_user_authorized:
            self.client.start()

    def send_message(self, username:str, message:str):

        async def send():
            await self.client.send_message('me', message)

        with self.client:
            self.client.loop.run_until_complete(send())
