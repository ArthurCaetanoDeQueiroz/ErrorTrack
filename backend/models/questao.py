from datetime import datetime
from extensions import db

class Questao(db.Model):
    __tablename__ = 'questao'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    enunciado = db.Column(db.Text, nullable=False)
    materia = db.Column(db.String(255), nullable=True)
    resposta = db.Column(db.Text, nullable=True)
    alternativa_correta = db.Column(db.String(255), nullable=False)
    alternativa_marcada = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def salvar(self):
        db.session.add(self)
        db.session.commit()

    def atualizar(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
        db.session.commit()

    def deletar(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def listar_todas(cls):
        return cls.query.all()

    @classmethod
    def buscar_por_id(cls, id_questao):
        return cls.query.get(id_questao)

    @classmethod
    def buscar_por_nome(cls, termo):
        return cls.query.filter(
            (cls.enunciado.ilike(f'%{termo}%')) | (cls.materia.ilike(f'%{termo}%'))
        ).all()

    def to_dict(self):
        return {
            'id': self.id,
            'enunciado': self.enunciado,
            'materia': self.materia,
            'resposta': self.resposta,
            'alternativa_correta': self.alternativa_correta,
            'alternativa_marcada': self.alternativa_marcada,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }