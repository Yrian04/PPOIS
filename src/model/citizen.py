from re import match


class Citizen:

    def __init__(self, name: str, income: int = 10):
        if not match(name, r'([A-Z][a-zA-Z]*) ([A-Z][a-zA-Z]*)'):
            raise ValueError("Invalid name")
        self._name = name
        if income <= 0:
            raise ValueError("Invalid name")
        self._income = income

    @property
    def name(self):
        return self._name

    @property
    def income(self):
        return self._income

    @income.setter
    def income(self, value: int):
        if value <= 0:
            raise ValueError
        self._income = value
