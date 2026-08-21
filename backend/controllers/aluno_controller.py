from flask import Blueprint, jsonify, request
from services.cadastrar_aluno_service import CadastrarAlunoService
from services.listar_alunos_service import ListarAlunosService
from services.buscar_aluno_por_id_service import BuscarAlunoPorIdService
from services.atualizar_aluno_service import AtualizarAlunoService
from services.excluir_aluno_service import ExcluirAlunoService
from services.buscar_alunos_por_nome_service import BuscarAlunosPorNomeService

aluno_bp = Blueprint('aluno', __name__)

class AlunoController:
    @staticmethod
    def listar_ou_buscar():
        nome = request.args.get('nome')
        if nome:
            resultado = BuscarAlunosPorNomeService().execute(nome)
        else:
            resultado = ListarAlunosService().execute()
        return jsonify(resultado), 200

    @staticmethod
    def buscar_por_id(id):
        resultado = BuscarAlunoPorIdService().execute(id)
        if resultado:
            return jsonify(resultado), 200
        return jsonify({'erro': 'Aluno não encontrado'}), 404

    @staticmethod
    def criar():
        data = request.get_json()
        try:
            resultado = CadastrarAlunoService().execute(data)
            return jsonify(resultado), 201
        except ValueError as e:
            return jsonify({'erro': str(e)}), 400

    @staticmethod
    def atualizar(id):
        data = request.get_json()
        resultado = AtualizarAlunoService().execute(id, data)
        if resultado:
            return jsonify(resultado), 200
        return jsonify({'erro': 'Aluno não encontrado'}), 404

    @staticmethod
    def deletar(id):
        sucesso = ExcluirAlunoService().execute(id)
        if sucesso:
            return jsonify({'mensagem': 'Aluno removido com sucesso'}), 200
        return jsonify({'erro': 'Aluno não encontrado'}), 404

aluno_bp.add_url_rule('/alunos', view_func=AlunoController.listar_ou_buscar, methods=['GET'])
aluno_bp.add_url_rule('/alunos/<int:id>', view_func=AlunoController.buscar_por_id, methods=['GET'])
aluno_bp.add_url_rule('/alunos', view_func=AlunoController.criar, methods=['POST'])
aluno_bp.add_url_rule('/alunos/<int:id>', view_func=AlunoController.atualizar, methods=['PUT'])
aluno_bp.add_url_rule('/alunos/<int:id>', view_func=AlunoController.deletar, methods=['DELETE'])