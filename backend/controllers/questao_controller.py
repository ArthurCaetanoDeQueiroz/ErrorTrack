from flask import Blueprint, request, jsonify
from services.cadastrar_questao_service import CadastrarQuestaoService
from models.questao import Questao

questao_bp = Blueprint('questao_bp', __name__)

@questao_bp.route('/questoes', methods=['POST'])
def criar():
    try:
        data = request.get_json()
        resultado = CadastrarQuestaoService().execute(data)
        return jsonify(resultado), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@questao_bp.route('/questoes', methods=['GET'])
def listar():
    try:
        termo = request.args.get('busca') or request.args.get('nome') or request.args.get('q')
        resultado = CadastrarQuestaoService().listar(termo)
        return jsonify(resultado), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@questao_bp.route('/questoes/<int:id>', methods=['GET'])
def buscar_por_id(id):
    try:
        questao = Questao.buscar_por_id(id)
        if not questao:
            return jsonify({'error': 'Questão não encontrada'}), 404
        return jsonify(questao.to_dict()), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@questao_bp.route('/questoes/relatorio-erros/<int:aluno_id>', methods=['GET'])
def relatorio_erros(aluno_id):
    try:
        return jsonify({
            'mensagem': f'Relatório de erros para o aluno ID {aluno_id}',
            'erros': []
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400