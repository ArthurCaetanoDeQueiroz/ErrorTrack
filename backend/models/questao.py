class Questao:
    def __init__(self, enunciado, alternativa_correta, alternativa_marcada=None, id=None):
        self.id = id
        self.enunciado = enunciado
        self.alternativa_correta = alternativa_correta
        self.alternativa_marcada = alternativa_marcada

    def save(self):
        pass

    @staticmethod
    def get_all():
        pass

    @staticmethod
    def get_by_id(questao_id):
        pass