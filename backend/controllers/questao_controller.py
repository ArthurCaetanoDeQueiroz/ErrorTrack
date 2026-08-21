from flask import Blueprint, jsonify, request
from services.cadastrar_questao_service import CadastrarQuestaoService
from services.listar_questoes_service import ListarQuestoesService
from services.buscar_questoes_por_simulado_service import BuscarQuestoesPorSimuladoService
from services.relatorio_erros_service import RelatorioErrosService

questao_bp = Blueprint('questao', __name__)

class QuestaoController:
    @staticmethod
    def listar_ou_buscar():
        simulado_id = request.args.get('simulado_id')
        if simulado_id:
            resultado = BuscarQuestoesPorSimuladoService().execute(simulado_id)
        else:
            resultado = ListarQuestoesService().execute()
        return jsonify(resultado), 200

    @staticmethod
    def criar():
        data = request.get_json()
        try:
            resultado = CadastrarQuestaoService().execute(data)
            return jsonify(resultado), 201
        except ValueError as e:
            return jsonify({'erro': str(e)}), 400

    @staticmethod
    def relatorio_erros(aluno_id):
        resultado = RelatorioErrosService().execute(aluno_id)
        return jsonify(resultado), 200

questao_bp.add_url_rule('/questoes', view_func=QuestaoController.listar_ou_buscar, methods=['GET'])
questao_bp.add_url_rule('/questoes', view_func=QuestaoController.criar, methods=['POST'])
questao_bp.add_url_rule('/questoes/relatorio-erros/<int:aluno_id>', view_func=QuestaoController.relatorio_erros, methods=['GET'])