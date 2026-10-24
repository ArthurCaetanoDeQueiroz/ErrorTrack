from models.aluno import Aluno

class AlunoRepository:
    def buscar_por_nome(self, nome):
        return Aluno.query.filter(Aluno.name.ilike(f'%{nome}%')).order_by(Aluno.name.asc()).all()
