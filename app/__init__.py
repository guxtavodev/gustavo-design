from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Crie as instâncias do Flask, SQLAlchemy e LoginManager
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Importe e registre as blueprints (rotas) da sua aplicação
from app.routes import pedidos_bp
app.register_blueprint(pedidos_bp)