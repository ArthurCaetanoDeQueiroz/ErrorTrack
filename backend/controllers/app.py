import os
import sys
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from models.aluno import Aluno, db

frontend_dir = os.path.abspath(os.path.join(root_dir, '..', 'frontend'))
app = Flask(__name__, static_folder=frontend_dir, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/ErrorTrack'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route('/alunos', methods=['POST'])
def criar_aluno():
    dados = request.get_json()

    if not dados or 'name' not in dados or 'materia' not in dados:
        return jsonify({'erro': 'Campos "name" e "materia" são obrigatórios'}), 400

    novo_aluno = Aluno(
        name=dados['name'],
        materia=dados['materia']
    )
    novo_aluno.salvar()

    return jsonify(novo_aluno.to_dict()), 201


@app.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = Aluno.query.all()
    return jsonify([a.to_dict() for a in alunos]), 200


@app.route('/alunos/<int:id>', methods=['GET'])
def buscar_aluno(id):
    a = Aluno.query.get(id)

    if not a:
        return jsonify({'erro': 'Aluno não encontrado'}), 404

    return jsonify(a.to_dict()), 200


@app.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    a = Aluno.query.get(id)

    if not a:
        return jsonify({'erro': 'Aluno não encontrado'}), 404

    dados = request.get_json()

    if not dados:
        return jsonify({'erro': 'Nenhum dado enviado'}), 400

    if 'name' in dados:
        a.name = dados['name']
    if 'materia' in dados:
        a.materia = dados['materia']

    db.session.commit()

    return jsonify(a.to_dict()), 200


@app.route('/alunos/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    a = Aluno.query.get(id)

    if not a:
        return jsonify({'erro': 'Aluno não encontrado'}), 404

    a.deletar()

    return jsonify({'mensagem': f'Aluno {id} removido com sucesso'}), 200


if __name__ == '__main__':
    app.run(debug=True)
