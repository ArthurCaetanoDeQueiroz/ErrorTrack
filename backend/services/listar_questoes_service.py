from models.questao import Questao

class ListarQuestoesService:
    def execute(self):
        questoes = Questao.listar_todos()
        return [q.to_dict() for q in questoes]