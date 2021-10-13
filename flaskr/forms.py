from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import InputRequired, DataRequired, Length, ValidationError, EqualTo


class LogInForm(FlaskForm):
    correo = StringField('Correo Electronico', validators=[InputRequired("Input is required!"), DataRequired("Data is required!")])
    password = PasswordField('Contraseña', validators=[InputRequired("Input is required!"), DataRequired("Data is required!")])
    submit = SubmitField('Iniciar Sesion')

class FilterForm(FlaskForm):
    name = StringField("Nombre", validators=[Length(max=15)])
    rol = SelectField("Rol", coerce=int)
    cargo = StringField("Cargo", validators=[Length(max=15)])
    date_admission = SelectField("Fecha Ingreso", coerce=int, choices=[(0, "---"), (1, "Antiguos a Recientes"), (2, "Recientes a Antiguos")])
    dependencia = StringField("Dependencia", validators=[Length(max=15)])
    submit = SubmitField("Filtro")

class ChangePassword(FlaskForm):
    oldpassword = PasswordField('* Contraseña antigua', validators=[InputRequired()])
    password = PasswordField('* Nueva contraseña', validators=[InputRequired(), EqualTo('confirm', message='Contraseñas deben ser iguales')])
    confirm  = PasswordField('* Confirmar nueva contraseña')
    submit = SubmitField("Cambiar contraseña")