from models.aluno import db

class Questao(db.Model):
    __tablename__ = 'questao'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    enunciado = db.Column(db.Text, nullable=False)
    alternativa_correta = db.Column(db.String(10), nullable=False)
    alternativa_marcada = db.Column(db.String(10), nullable=True)

    def salvar(self):
        db.session.add(self)
        db.session.commit()

    def atualizar(self, enunciado=None, alternativa_correta=None, alternativa_marcada=None):
        if enunciado:
            self.enunciado = enunciado
        if alternativa_correta:
            self.alternativa_correta = alternativa_correta
        if alternativa_marcada:
            self.alternativa_marcada = alternativa_marcada
        db.session.commit()

    def deletar(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def listar_todos(cls):
        return cls.query.all()

    @classmethod
    def buscar_por_id(cls, id_questao):
        return cls.query.get(id_questao)

    def to_dict(self):
        return {
            'id': self.id,
            'enunciado': self.enunciado,
            'alternativa_correta': self.alternativa_correta,
            'alternativa_marcada': self.alternativa_marcada
        }