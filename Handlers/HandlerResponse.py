from typing import Union
from discord.ext.commands import Context
from Config.Exceptions import musicError
from discord import Embed, Interaction
from UI.Views.AbstractView import AbstractView


class HandlerResponse:
    def __init__(self, ctx: Union[Context, Interaction], embed: Embed = None, error: musicError = None, view=None) -> None:
        self.__ctx: Context = ctx
        self.__error: musicError = error
        self.__embed: Embed = embed
        self.__success = False if error else True
        self.__view = view

    @property
    def ctx(self) -> Union[Context, Interaction]:
        return self.__ctx

    @property
    def embed(self) -> Union[Embed, None]:
        return self.__embed

    @property
    def view(self) -> AbstractView:
        return self.__view

    def error(self) -> Union[musicError, None]:
        return self.__error

    @property
    def success(self) -> bool:
        return self.__success
