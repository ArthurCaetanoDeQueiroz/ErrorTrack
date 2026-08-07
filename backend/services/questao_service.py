from models.questao import Questao
from repositories.questao_repository import QuestaoRepository

class QuestaoService:
    def __init__(self):
        self.repository = QuestaoRepository()

    def listar_todas(self):
        return Questao.get_all()

    def obter_por_id(self, id):
        return Questao.get_by_id(id)

    def criar_questao(self, data):
        questao = Questao(
            enunciado=data.get('enunciado'),
            alternativa_correta=data.get('alternativa_correta')
        )
        return questao.save()

    def buscar_por_simulado(self, simulado_id):
        return self.repository.buscar_questoes_por_simulado_procedure(simulado_id)

    def relatorio_erros(self, aluno_id):
        return self.repository.gerar_relatorio_erros_procedure(aluno_id)