from citizen import Citizen


class Government:
    def __init__(self, head: Citizen):
        self._head: Citizen = head

    @property
    def head(self):
        return self._head

    def change_head(self, head: Citizen):
        self._head = head

    def provide_security(self, citizen: Citizen):
        print(f"Security of {citizen.name} is provided thanks {self.head.name}!")

    def provided_social_security(self, citizen: Citizen):
        print(f"Social security of {citizen.name} is provided thanks {self.head.name}!")
