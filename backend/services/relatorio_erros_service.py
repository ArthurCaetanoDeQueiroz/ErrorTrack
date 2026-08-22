from repositories.questao_repository import QuestaoRepository

class RelatorioErrosService:
    def __init__(self):
        self.repository = QuestaoRepository()

    def execute(self, aluno_id):
        return self.repository.gerar_relatorio_erros_procedure(aluno_id)