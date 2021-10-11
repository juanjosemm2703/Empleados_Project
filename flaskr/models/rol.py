from uuid import uuid4

from sqlalchemy.orm import validates
from flaskr.sqla import sqla


class Rol(sqla.Model):
    id_rol = sqla.Column(sqla.Integer, primary_key=True, nullable=False)
    tipo = sqla.Column(sqla.Text, nullable=False, unique=True)

    def __repr__(self):
        return self.tipo
