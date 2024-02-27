import abc

from src.DAO.repository import Repository
from input import Input


class Command(abc.ABC):
    _name: str = "command"
    _help: str = "Help for this command"

    def __init__(self, input_: Input, repository: Repository):
        self._repository = Repository
        self._args = input_.args

    @property
    def name(self):
        return self._name

    @property
    def help(self):
        return self._help

    @property
    def args(self):
        return self._args.copy()

    @abc.abstractmethod
    def execute(self): pass

    @abc.abstractmethod
    def can_execute(self, *args: str) -> bool: pass
