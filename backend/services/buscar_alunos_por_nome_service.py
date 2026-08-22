from repositories.aluno_repository import AlunoRepository

class BuscarAlunosPorNomeService:
    def __init__(self):
        self.repository = AlunoRepository()

    def execute(self, nome):
        return self.repository.buscar_por_nome_procedure(nome)