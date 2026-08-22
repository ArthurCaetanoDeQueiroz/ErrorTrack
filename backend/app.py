import os
import sys

root_dir = os.path.abspath(os.path.dirname(__file__))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from flask import Flask
from extensions import db
from routes import register_routes

frontend_dir = os.path.abspath(os.path.join(root_dir, '..', 'frontend'))

app = Flask(__name__, static_folder=frontend_dir, static_url_path='')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///errortrack.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
register_routes(app)

with app.app_context():
    db.create_all()

@app.route('/')
def home():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)