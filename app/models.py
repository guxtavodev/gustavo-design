from app import db, app

class Pedidos(db.Model):
  nome = db.Column(db.String(100))
  id = db.Column(db.String(), primary_key=True)
  tipoArte = db.Column(db.String())
  idVisual = db.Column(db.String())
  prazo = db.Column(db.String())
  objetivo = db.Column(db.String())
  publicoAlvo = db.Column(db.String())
  referencias = db.Column(db.String())
  contato = db.Column(db.String())
  
  def __init__(self, nome, id, tipoArte, idVisual, prazo, objetivo, publicoAlvo, referencias, contato):
    self.nome = nome 
    self.id = id 
    self.tipoArte = tipoArte
    self.idVisual = idVisual
    self.prazo = prazo
    self.objetivo = objetivo
    self.publicoAlvo = publicoAlvo
    self.referencias = referencias
    self.contato = contato
    
class Clientes(db.Model):
  nome = db.Column(db.String())
  telefone = db.Column(db.String(), primary_key=True)
  
  def __init__(self, nome, telefone):
    self.nome = nome 
    self.telefone = telefone

with app.app_context():
  db.create_all()