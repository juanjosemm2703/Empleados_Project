from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import InputRequired, DataRequired, Length, ValidationError, EqualTo


class LogInForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[InputRequired("Input is required!"), DataRequired("Data is required!")])
    password = PasswordField('Contraseña', validators=[InputRequired("Input is required!"), DataRequired("Data is required!")])
    submit = SubmitField('Iniciar Sesion')

class FilterForm(FlaskForm):
    name = StringField("Nombre", validators=[Length(max=15)])
    rol = SelectField("Rol", coerce=int)
    cargo = StringField("Cargo", validators=[Length(max=15)])
    date_admission = SelectField("Fecha Ingreso", coerce=int, choices=[(0, "---"), (1, "Max a Min"), (2, "Min a Max")])
    dependencia = StringField("Dependencia", validators=[Length(max=15)])
    submit = SubmitField("Filtro")

class ChangePassword(FlaskForm):
    password = PasswordField('New Password', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm  = PasswordField('Repeat Password')