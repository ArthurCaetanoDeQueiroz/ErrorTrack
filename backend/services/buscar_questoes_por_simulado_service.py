from repositories.questao_repository import QuestaoRepository

class BuscarQuestoesPorSimuladoService:
    def __init__(self):
        self.repository = QuestaoRepository()

    def execute(self, simulado_id):
        return self.repository.buscar_questoes_por_simulado_procedure(simulado_id)