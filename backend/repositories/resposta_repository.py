from models.resposta_aluno import RespostaAluno

class RespostaRepository:
    def listar_por_aluno(self, aluno_id):
        return RespostaAluno.query.filter_by(aluno_id=aluno_id).order_by(RespostaAluno.respondida_em.desc()).all()
