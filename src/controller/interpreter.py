from command import Command
from input import Input


class Interpreter:
    def __init__(self, commands: dict[str, Command]):
        self._commands = commands

    def interpret(self, input_: Input):
        try:
            self._commands[input_.command_name].execute(*input_.args)
        except Exception as ex:
            raise ex.add_note("Command execution error")
