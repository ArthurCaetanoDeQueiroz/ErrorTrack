from models.aluno import Aluno

class AtualizarAlunoService:
    def execute(self, aluno_id, dados):
        aluno = Aluno.buscar_por_id(aluno_id)
        if not aluno:
            return None
        aluno.atualizar(name=dados.get('name'), materia=dados.get('materia'))
        return aluno.to_dict()