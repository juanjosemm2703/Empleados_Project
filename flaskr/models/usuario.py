from uuid import uuid4

from datetime import datetime
from sqlalchemy.orm import validates
from flaskr.sqla import sqla
from werkzeug.security import check_password_hash, generate_password_hash


class Usuario(sqla.Model):
    id_usuario = sqla.Column(sqla.Integer, primary_key=True, nullable=False)
    correo = sqla.Column(sqla.Text, nullable=False, unique=True)
    password = sqla.Column(sqla.Text, nullable=False)
    nombre = sqla.Column(sqla.Text, nullable=False)
    apellido = sqla.Column(sqla.Text, nullable=False)
    cedula = sqla.Column(sqla.Integer, nullable=False)
    fecha_ingreso = sqla.Column(sqla.DateTime, nullable=False)
    fecha_contrato = sqla.Column(sqla.DateTime, nullable=False)
    tipo_contrato = sqla.Column(sqla.Text, nullable=False)
    cargo = sqla.Column(sqla.Text, nullable=False)
    dependencia = sqla.Column(sqla.Text, nullable=False)
    salario = sqla.Column(sqla.Float, nullable=False)
    estado = sqla.Column(sqla.Float, nullable=False, default=True)
    uuid = sqla.Column(sqla.String(64), nullable=False, default=lambda: str(uuid4()))
    id_rol = sqla.Column(sqla.Integer, sqla.ForeignKey('rol.id_rol'), nullable=False)
    rol = sqla.relationship('Rol', backref=sqla.backref('usuarios', lazy=True))



    @validates('correo', 'password', 'nombre', 'apellido', 'cedula', 'fecha_ingreso', 'fecha_contrato', 'tipo_contrato', 'cargo', 'dependencia', 'salario', 'id_rol')
    def validate_not_empty(self, key, value):
        if not value:
            raise ValueError(f'{key.capitalize()} is required.')
        return value

        if key == 'correo':
            self.validate_is_unique(key, value, error_message=f'{value} already registered')

        if key == 'password':
            value = generate_password_hash(value)

        return value

    def validate_is_unique(self, key, value, error_message=None):
        if (
                Usuario.query.filter_by(**{key: value}).first()
                is not None
        ):
            if not error_message:
                error_message = f'{key} debe ser unico'
            raise ValueError(error_message)


    def correct_password(self, plaintext):
        return check_password_hash(self.password, plaintext)

    def get_id(self):
        return self.uuid

    def __repr__(self):
        return self.id_usuario

