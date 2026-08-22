from models.aluno import Aluno

class CadastrarAlunoService:
    def execute(self, dados):
        if not dados.get('name') or not dados.get('materia'):
            raise ValueError("Campos 'name' e 'materia' são obrigatórios.")
        
        novo_aluno = Aluno(name=dados['name'], materia=dados['materia'])
        novo_aluno.salvar()
        return novo_aluno.to_dict()