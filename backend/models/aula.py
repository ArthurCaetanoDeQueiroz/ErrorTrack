class Aula:
    def __init__(self, data, tema, id=None):
        self.id = id
        self.data = data
        self.tema = tema

    def save(self):
        pass

    @staticmethod
    def get_all():
        pass

    @staticmethod
    def get_by_id(aula_id):
        pass