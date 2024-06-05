from . import db

class Foro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_comunidad = db.Column(db.Integer, nullable=False)
    id_usuario = db.Column(db.Integer, nullable=False)
    tipo_foro = db.Column(db.String(50), nullable=False)
    estado_foro = db.Column(db.String(50), nullable=False)
    tema_foro = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<Foro {self.tema_foro}>'
