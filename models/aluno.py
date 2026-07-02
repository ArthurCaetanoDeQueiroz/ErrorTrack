from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Aluno(db.Model):
    __tablename__ = 'aluno'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    materia = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
 
    def salvar(self):
        db.session.add(self)
        db.session.commit()
 
    def deletar(self):
        db.session.delete(self)
        db.session.commit()
 
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'materia': self.materia,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
 
    def __repr__(self):
        return f'<Aluno {self.id} - {self.name}>'