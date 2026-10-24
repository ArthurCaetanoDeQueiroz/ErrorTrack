from sqlalchemy import func, case
from extensions import db
from models.questao import Questao
from models.resposta_aluno import RespostaAluno

class QuestaoRepository:
    def buscar_com_filtros(self, termo=None, materia=None):
        consulta = Questao.query
        if termo:
            consulta = consulta.filter(Questao.enunciado.ilike(f'%{termo}%'))
        if materia:
            consulta = consulta.filter(Questao.materia.ilike(f'%{materia}%'))
        return consulta.order_by(Questao.id.desc()).all()

    def gerar_relatorio_erros(self, aluno_id=None):
        consulta = RespostaAluno.query.filter(RespostaAluno.correta.is_(False))
        if aluno_id is not None:
            consulta = consulta.filter(RespostaAluno.aluno_id == aluno_id)
        return [resposta.to_dict() for resposta in consulta.order_by(RespostaAluno.respondida_em.desc()).all()]

    def resumo_desempenho(self, aluno_id=None):
        consulta = db.session.query(
            func.count(RespostaAluno.id),
            func.sum(case((RespostaAluno.correta.is_(True), 1), else_=0)),
            func.sum(case((RespostaAluno.correta.is_(False), 1), else_=0))
        )
        if aluno_id is not None:
            consulta = consulta.filter(RespostaAluno.aluno_id == aluno_id)
        total, corretas, erros = consulta.one()
        total = total or 0
        corretas = int(corretas or 0)
        erros = int(erros or 0)
        return {
            'total_respostas': total,
            'acertos': corretas,
            'erros': erros,
            'percentual_acerto': round(corretas * 100 / total, 1) if total else 0
        }
