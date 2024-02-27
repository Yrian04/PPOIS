from typing import Callable

from command import Command
from input import Input
from src.DAO.repository import Repository


class Interpreter:
    def __init__(self, commands: dict[str, Callable[[Input, Repository], Command]]):
        self._commands = commands

    def interpret(self, input_: Input, repository: Repository) -> Command:
        try:
            return self._commands[input_.command_name](input_, repository)
        except Exception as ex:
            raise ex.add_note("Command interpretation error")
