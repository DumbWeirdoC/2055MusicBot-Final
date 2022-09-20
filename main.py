from Music.ArioInitializer import ArioInitializer
from Config.Folder import Folder

if __name__ == '__main__':
    folder = Folder()
    initializer = ArioInitializer(willListen=True)
    musicBot = initializer.getBot()
    musicBot.startBot()