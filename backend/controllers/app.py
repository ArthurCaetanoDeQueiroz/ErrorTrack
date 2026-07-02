from flask import Flask, jsonify, request, render_template, send_from_directory, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from models import aluno
db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/ErrorTrack'

@app.route('/alunos', methods=['POST'])
def criar_aluno():
    dados = request.get_json()
 
    if not dados or 'name' not in dados or 'materia' not in dados:
        return jsonify({'erro': 'Campos "name" e "materia" são obrigatórios'}), 400
 
    novo_aluno = aluno(
        name=dados['name'],
        materia=dados['materia']
    )
    novo_aluno.salvar()
 
    return jsonify(novo_aluno.to_dict()), 201
 
 
# READ - Listar todos os alunos
@app.route('/alunos', methods=['GET'])
def listar_alunos():
    alunos = aluno.query.all()
    return jsonify([a.to_dict() for a in alunos]), 200
 
 
# READ - Buscar um aluno pelo id
@app.route('/alunos/<int:id>', methods=['GET'])
def buscar_aluno(id):
    a = aluno.query.get(id)
 
    if not a:
        return jsonify({'erro': 'Aluno não encontrado'}), 404
 
    return jsonify(a.to_dict()), 200
 
 
# UPDATE - Atualizar um aluno existente
@app.route('/alunos/<int:id>', methods=['PUT'])
def atualizar_aluno(id):
    a = aluno.query.get(id)
 
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
 
 
# DELETE - Remover um aluno
@app.route('/alunos/<int:id>', methods=['DELETE'])
def deletar_aluno(id):
    a = aluno.query.get(id)
 
    if not a:
        return jsonify({'erro': 'Aluno não encontrado'}), 404
 
    a.deletar()
 
    return jsonify({'mensagem': f'Aluno {id} removido com sucesso'}), 200
 
 
if __name__ == '__main__':
    app.run(debug=True)
