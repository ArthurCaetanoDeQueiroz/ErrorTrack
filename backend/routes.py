from controllers.aluno_controller import aluno_bp
from controllers.questao_controller import questao_bp

def register_routes(app):
    app.register_blueprint(aluno_bp)
    app.register_blueprint(questao_bp)