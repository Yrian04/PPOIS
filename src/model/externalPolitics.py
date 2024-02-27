from externalRelation import ExternalRelation


class ExternalPolitics:
    from state import State

    def __init__(self):
        self._external_relations = []

    def add_external_relation(self, external_relation: ExternalRelation):
        self._external_relations.append(external_relation)

    def get_external_relation(self, state: State):
        try:
            return filter(lambda x: x.other_state == state, self._external_relations)[0]
        except IndexError:
            raise ValueError()

    def remove_external_relation(self, external_relation: ExternalRelation):
        self._external_relations.remove(external_relation)
