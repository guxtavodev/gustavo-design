from flask import Blueprint

pedidos_bp = Blueprint('pedidos', __name__)
produtos_bp = Blueprint('produtos', __name__)

from app.routes import pedidos, produtos