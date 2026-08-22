from models.questao import Questao

class CadastrarQuestaoService:
    def execute(self, dados):
        if not dados.get('enunciado') or not dados.get('alternativa_correta'):
            raise ValueError("Enunciado e alternativa_correta são obrigatórios.")

        nova_questao = Questao(
            enunciado=dados['enunciado'],
            materia=dados.get('materia'),
            alternativa_correta=dados['alternativa_correta'],
            alternativa_marcada=dados.get('alternativa_marcada')
        )
        nova_questao.salvar()
        return nova_questao.to_dict()

    def listar(self, termo=None):
        if termo:
            questoes = Questao.buscar_por_nome(termo)
        else:
            questoes = Questao.listar_todas()
        return [q.to_dict() for q in questoes]