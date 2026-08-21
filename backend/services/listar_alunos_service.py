from models.aluno import Aluno

class ListarAlunosService:
    def execute(self):
        alunos = Aluno.listar_todos()
        return [aluno.to_dict() for aluno in alunos]