from infrastructure import Infrastructure
from citizen import Citizen


class Economy:
    def __init__(self, treasury: int = 0):
        self._infrastructure = Infrastructure()
        self._treasury = treasury

    @property
    def treasury(self):
        return self._treasury

    def enhance_infrastructure(self):
        if self.treasury < self._infrastructure.get_cost_of_enhancing():
            raise AttributeError
        self._infrastructure.enhance()

    def collect_taxes(self, citizen: Citizen):
        self._treasury += citizen.income // (20*self._infrastructure.level)
