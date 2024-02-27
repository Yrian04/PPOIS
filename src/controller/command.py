import abc

from src.DAO.repository import Repository


class Command(abc.ABC):
    _name: str = "command"
    _help: str = "Help for this command"

    def __init__(self, repository: Repository):
        self._repository = Repository

    @property
    def name(self):
        return self._name

    @property
    def help(self):
        return self._help

    @abc.abstractmethod
    def execute(self, *args: str): pass

    @abc.abstractmethod
    def cen_execute(self, *args: str) -> bool: pass
