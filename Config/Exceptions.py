from Config.Messages import Messages


class musicError(Exception):
    def __init__(self, message='', title='', *args: object) -> None:
        self.__message = message
        self.__title = title
        super().__init__(*args)

    @property
    def message(self) -> str:
        return self.__message

    @property
    def title(self) -> str:
        return self.__title


class ImpossibleMove(musicError):
    def __init__(self, message='', title='', *args: object) -> None:
        message = Messages()
        if title == '':
            title = message.IMPOSSIBLE_MOVE
        super().__init__(message, title, *args)


class MusicUnavailable(musicError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class YoutubeError(musicError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class BadCommandUsage(musicError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class DownloadingError(musicError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class SpotifyError(musicError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class DeezerError(musicError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class UnknownError(musicError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class InvalidInput(musicError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class WrongLength(musicError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class ErrorMoving(musicError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class ErrorRemoving(musicError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class InvalidIndex(musicError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)


class NumberRequired(musicError):
    def __init__(self, message='', title='', *args: object) -> None:
        super().__init__(message, title, *args)
