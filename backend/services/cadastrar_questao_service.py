from models.questao import Questao

class CadastrarQuestaoService:
    def execute(self, dados):
        if not dados.get('enunciado') or not dados.get('alternativa_correta'):
            raise ValueError("Enunciado e alternativa_correta são obrigatórios.")

        nova_questao = Questao(
            enunciado=dados['enunciado'],
            alternativa_correta=dados['alternativa_correta'],
            alternativa_marcada=dados.get('alternativa_marcada')
        )
        nova_questao.salvar()
        return nova_questao.to_dict()