from flask import Flask
from extensions import db
from routes import register_routes

from models.aluno import Aluno
from models.aula import Aula
from models.questao import Questao
from models.simulado import Simulado
from models.mapa_erro import MapaErro

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///errortrack.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

register_routes(app)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)