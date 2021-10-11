from datetime import datetime
from sqlalchemy.orm import validates
from flaskr.sqla import sqla



class Retroalimentacion(sqla.Model):
    idRetroalimentacion = sqla.Column(sqla.Integer, primary_key=True, nullable=False)
    idEmpleado = sqla.Column(sqla.Integer, sqla.ForeignKey('usuario.idUsuario'), nullable=False)
    idAdministrador = sqla.Column(sqla.Text, sqla.ForeignKey('usuario.idUsuario'), nullable=False)
    comentario = sqla.Column(sqla.Text, nullable=False)
    puntaje = sqla.Column(sqla.Integer, nullable=False)
    fecha = sqla.Column(sqla.DateTime, nullable=False, default=datetime.utcnow)

    @validates('title', 'body')
    def validate_not_empty(self, key, value):
        if not value:
            raise ValueError(f'{key.capitalize()} is required.')
        return value

    def __repr__(self):
        return self.comentario
