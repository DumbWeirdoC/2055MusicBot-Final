import os
from decouple import config
from Config.Singleton import Singleton
from Config.Folder import Folder


class VConfigs(Singleton):
    def __init__(self) -> None:
        if not super().created:
            self.BOT_PREFIX = '!'
            try:
                self.BOT_TOKEN = config('BOT_TOKEN')
                self.SPOTIFY_ID = config('SPOTIFY_ID')
                self.SPOTIFY_SECRET = config('SPOTIFY_SECRET')
                self.BOT_PREFIX = config('BOT_PREFIX')
            except:
                print(
                    '[ERROR] -> You must create and .env file with all required fields, see documentation for help')

            self.CLEANER_MESSAGES_QUANT = 5
            self.ACQUIRE_LOCK_TIMEOUT = 10
            self.QUEUE_VIEW_TIMEOUT = 120
            self.COMMANDS_FOLDER_NAME = 'DiscordCogs'
            self.COMMANDS_PATH = f'{Folder().rootFolder}{self.COMMANDS_FOLDER_NAME}'
            self.VC_TIMEOUT = 300

            self.CHANCE_SHOW_PROJECT = 15
            self.PROJECT_URL = 'https://github.com/DumbWeirdoC/2055MusicBot-Final'
            self.SUPPORTING_ICON = 'https://i.ibb.co/PZs18HZ/IMG-9334.jpg'

            self.MAX_PLAYLIST_LENGTH = 50
            self.MAX_PLAYLIST_FORCED_LENGTH = 5
            self.MAX_SONGS_IN_PAGE = 10
            self.MAX_PRELOAD_SONGS = 15
            self.MAX_SONGS_HISTORY = 15

            self.INVITE_MESSAGE = """To invite 2055-Music, to your own server, click [here]({}). 
            Or use this direct URL: {}"""

            self.MY_ERROR_BAD_COMMAND = 'This string serves to verify if some error was raised by myself on purpose'
            self.INVITE_URL = 'https://discordapp.com/oauth2/authorize?client_id={}&scope=bot'

    def getProcessManager(self):
        return self.__manager

    def setProcessManager(self, newManager):
        self.__manager = newManager
