import dbm
import os.path
import shelve

from repository import Repository
from src.model.state import State


class FileRepository(Repository):
    def __init__(self, file_name: str):
        if not os.path.exists(file_name):
            raise ValueError("File is not exist")
        self.file: str = file_name

    def get_states(self):
        with shelve.open(self.file, "r") as file:
            return file.values()

    def get_state(self, name: str):
        with shelve.open(self.file, "r") as file:
            if name not in file:
                raise ValueError("No state with this name")
            return file[name]

    def add_state(self, state: State):
        with shelve.open(self.file, "w") as file:
            file[state.name] = state

    def remove_state(self, state: State):
        with shelve.open(self.file, "w") as file:
            if state.name not in file:
                raise ValueError("No state with this name")
            del file[state.name]
