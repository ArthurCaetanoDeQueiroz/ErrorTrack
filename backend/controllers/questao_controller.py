from flask import Blueprint, jsonify, request
from services.questao_service import QuestaoService

questao_bp = Blueprint('questao', __name__)
questao_service = QuestaoService()

@questao_bp.route('/questoes', methods=['GET'])
def get_questoes():
    simulado_id = request.args.get('simulado_id')
    if simulado_id:
        questoes = questao_service.buscar_por_simulado(simulado_id)
    else:
        questoes = questao_service.listar_todas()
    return jsonify(questoes), 200

@questao_bp.route('/questoes/<int:id>', methods=['GET'])
def get_questao(id):
    questao = questao_service.obter_por_id(id)
    if questao:
        return jsonify(questao), 200
    return jsonify({'erro': 'Questão não encontrada'}), 404

@questao_bp.route('/questoes', methods=['POST'])
def create_questao():
    data = request.get_json()
    nova_questao = questao_service.criar_questao(data)
    return jsonify(nova_questao), 201

@questao_bp.route('/questoes/relatorio-erros/<int:aluno_id>', methods=['GET'])
def get_relatorio_erros(aluno_id):
    relatorio = questao_service.relatorio_erros(aluno_id)
    return jsonify(relatorio), 200