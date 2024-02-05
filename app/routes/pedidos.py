from flask import render_template, request, jsonify
import uuid
from app.models import Pedidos
from app.routes import pedidos_bp
from app import db

@pedidos_bp.route("/")
def homepage():
  return render_template("index.html")
  
@pedidos_bp.route("/api/enviar-pedido", methods=["POST"])
def enviarPedido():
  nome = request.form["nome"]
  id = str(uuid.uuid4())
  tipoArte = request.form["tipoArte"]
  idVisual = request.form["idVisual"]
  prazo = request.form["prazo"]
  objetivo = request.form["objetivo"]
  publicoAlvo = request.form["publico"]
  referencias = request.form["referencias"]
  contato = request.form["contato"]
  
  newPedido = Pedidos(nome=nome, id=id, tipoArte=tipoArte, idVisual=idVisual, prazo=prazo, objetivo=objetivo, publicoAlvo=publicoAlvo, referencias=referencias, contato=contato)
  db.session.add(newPedido)
  db.session.commit()