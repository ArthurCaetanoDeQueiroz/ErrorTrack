from flask import Blueprint, jsonify, request
from services.aluno_service import AlunoService

aluno_bp = Blueprint('aluno', __name__)
aluno_service = AlunoService()

@aluno_bp.route('/alunos', methods=['GET'])
def get_alunos():
    nome = request.args.get('nome')
    if nome:
        alunos = aluno_service.buscar_alunos_por_nome(nome)
    else:
        alunos = aluno_service.listar_todos()
    return jsonify(alunos), 200

@aluno_bp.route('/alunos/<int:id>', methods=['GET'])
def get_aluno(id):
    aluno = aluno_service.obter_por_id(id)
    if aluno:
        return jsonify(aluno), 200
    return jsonify({'erro': 'Aluno não encontrado'}), 404

@aluno_bp.route('/alunos', methods=['POST'])
def create_aluno():
    data = request.get_json()
    novo_aluno = aluno_service.criar_aluno(data)
    return jsonify(novo_aluno), 201