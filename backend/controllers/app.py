import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from Flask import Flask
from models.aluno import db
from controllers.aluno_controller import aluno_bp
from controllers.questao_controller import questao_bp

frontend_dir = os.path.abspath(os.path.join(root_dir, '..', 'frontend'))

app = Flask(__name__, static_folder=frontend_dir, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/ErrorTrack'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(aluno_bp)
app.register_blueprint(questao_bp)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)