from flask import Blueprint

pedidos_bp = Blueprint('pedidos', __name__)

from app.routes import pedidos