from re import match

from externalPolitics import ExternalPolitics
from legislation import Legislation
from government import Government
from economy import Economy
from population import Population


class State:
    from citizen import Citizen

    def __init__(self, name: str, head: Citizen):
        self._name: str = name
        self._government: Government = Government(head)
        self._economy: Economy = Economy()
        self._legislation: Legislation = Legislation()
        self._population: Population = Population()
        self._external_politics: ExternalPolitics = ExternalPolitics()

        self._population.add_citizen(head)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if match(value, r'((([A-Z][a-zA-Z]*) )|of |the )*(([A-Z][a-zA-Z]*))'):
            self._name = value
        else:
            raise ValueError

    @property
    def government(self):
        return self._government

    @property
    def economy(self):
        return self._economy

    @property
    def legislation(self):
        return self._legislation

    @property
    def population(self):
        return self._population

    @property
    def external_politics(self):
        return self._external_politics
