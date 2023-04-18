from ..formulario import db

class Meta(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cidade = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(50), nullable=False)
    responsavel = db.Column(db.String(50), nullable=False)
    data_ini_meta = db.Column(db.Date, nullable=False)
    data_fim_meta = db.Column(db.Date, nullable=False)
    valor = db.Column(db.float, nullable=False)
    agente_id = db.Column(db.Integer, nullable=False)
