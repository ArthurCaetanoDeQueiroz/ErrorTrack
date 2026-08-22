from models.aluno import Aluno

class AlunoRepository:
    def buscar_por_nome_procedure(self, nome):
        alunos = Aluno.query.filter(Aluno.name.ilike(f"%{nome}%")).all()
        return [aluno.to_dict() for aluno in alunos]