from models.aluno import Aluno
from repositories.aluno_repository import AlunoRepository

class AlunoService:
    def __init__(self):
        self.repository = AlunoRepository()

    def listar_todos(self):
        return Aluno.get_all()

    def obter_por_id(self, aluno_id):
        return Aluno.get_by_id(aluno_id)

    def criar_aluno(self, data):
        aluno = Aluno(nome=data.get('nome'), matricula=data.get('matricula'))
        return aluno.save()

    def buscar_alunos_por_nome(self, nome):
        return self.repository.buscar_por_nome_procedure(nome)