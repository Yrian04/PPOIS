from law import Law


class Legislation:
    def __init__(self):
        self._laws: list[Law] = []

    def publish_law(self, law: Law):
        self._laws.append(law)

    def repeal_law(self, law: Law):
        self._laws.remove(law)

    def get_laws(self):
        return self._laws.copy()

    def make_amendment(self, law: Law, amendment: str):
        law.text += "\nAMENDMAENT\n" + amendment
