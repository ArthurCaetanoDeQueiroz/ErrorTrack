from extensions import db

class Simulado:
    def __init__(self, aula_id, id=None):
        self.id = id
        self.aula_id = aula_id

    def save(self):
        pass

    @staticmethod
    def get_all():
        pass

    @staticmethod
    def get_by_id(simulado_id):
        pass