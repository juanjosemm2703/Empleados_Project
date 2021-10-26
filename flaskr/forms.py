from flask_wtf import FlaskForm
from wtforms import StringField, FileField, PasswordField, DecimalField, SubmitField, SelectField, HiddenField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import InputRequired, DataRequired, Length, Email, ValidationError, EqualTo
from wtforms.fields.html5 import EmailField, DateField, IntegerField
from flask_wtf.file import FileAllowed
from markupsafe import Markup
from wtforms.widgets import Input
import re

class PriceInput(Input):
    input_type = "number"

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        kwargs.setdefault('type', self.input_type)
        kwargs.setdefault("step", "100")
        if 'value' not in kwargs:
            kwargs['value'] = field._value()
        if 'required' not in kwargs and 'required' in getattr(field, 'flags', []):
            kwargs['required'] = True
        return Markup("""
                <div class="input-group mb-3">
                    <div class="input-group-prepend">
                        <span class="input-group-text">$</span>
                    </div>
                    <input %s>
                </div>""" % self.html_params(name=field.name, **kwargs))

class SalarioField(DecimalField):
    widget = PriceInput()

class TelInput(Input):
    input_type = 'tel'
    
class TelField(IntegerField):
    widget = TelInput()
    
class LogInForm(FlaskForm):
    correo = StringField('Usuario (Correo Electrónico)', validators=[InputRequired("Este campo no puede estar vacío"), DataRequired("Este campo no puede estar vacio")])
    password = PasswordField('Contraseña', validators=[InputRequired("Este campo no puede estar vacío"), DataRequired("Este campo no puede estar vacio")])
    submit = SubmitField('Iniciar Sesion')

class ForgotPasswordForm(FlaskForm):
    email = EmailField('Correo Electrónico', validators=[InputRequired("Este campo no puede estar vacío"), DataRequired("Este campo no puede estar vacio")])
    submit = SubmitField('Restablecer Contraseña')

def password_validate(form, field):
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%&-_])[A-Za-z\d@#$%&-_]{8,20}$"
    patron = re.compile(reg)
    match = re.search(patron, field.data)
    if not match:
        raise ValidationError("La contraseña debe tener entre 8 y 20 caracteres; y debe incluir al menos una mayuscula, una minuscula y un caracter especial (@#$%&-_).")

class FilterForm(FlaskForm):
    name = StringField("Nombre", validators=[Length(max=15)])
    rol = SelectField("Rol", coerce=int)
    cargo = StringField("Cargo", validators=[Length(max=15)])
    date_admission = SelectField("Fecha Ingreso", coerce=int, choices=[(0, "---"), (1, "Antiguos a Recientes"), (2, "Recientes a Antiguos")])
    dependencia = StringField("Dependencia", validators=[Length(max=15)])
    submit = SubmitField("Filtro")

class ChangePassword(FlaskForm):
    oldpassword = PasswordField('* Contraseña actual', validators=[InputRequired("Este campo no puede estar vacio")])
    password = PasswordField('* Nueva contraseña', validators=[InputRequired("Este campo no puede estar vacio"), password_validate, EqualTo('confirm', message='Contraseñas deben ser iguales')])
    confirm  = PasswordField('* Confirmar nueva contraseña', validators=[InputRequired("Este campo no puede estar vacio")])
    submit = SubmitField("Cambiar contraseña")
    
class NewUserForm(FlaskForm):
    correo = EmailField("Email",  validators=[InputRequired("Por favor ingrese su correo electronico"), Email("Por favor ingrese un correo electronico valido")])
    nombre = StringField("Nombre", validators=[InputRequired("Este campo no puede estar vacio")])
    apellido = StringField("Apellido", validators=[InputRequired("Este campo no puede estar vacio")])
    cedula = IntegerField("Cedula", validators=[InputRequired("Este campo no puede estar vacio")])
    fecha_ingreso = DateField("Fecha Ingreso", validators=[InputRequired("Este campo no puede estar vacio")])
    fecha_contrato = DateField("Fecha de finalizacion del contrato", validators=[InputRequired("Este campo no puede estar vacio")])
    tipo_contrato = StringField("Tipo de contrato", validators=[InputRequired("Este campo no puede estar vacio")])
    cargo = StringField("Cargo", validators=[InputRequired("Este campo no puede estar vacio")])
    dependencia = StringField("Dependencia", validators=[InputRequired("Este campo no puede estar vacio")])
    salario = SalarioField("Salario", validators=[InputRequired("Este campo no puedede estar vacio")])
    idRol = SelectField("Rol", coerce=int, validators=[InputRequired("Este campo no puede estar vacio"), DataRequired("Este campo no puede estar vacio")])
    direccion = StringField("Direccion", validators=[InputRequired("Este campo no puede estar vacio")])
    celular = TelField("Celular", validators=[InputRequired("Este campo no puede estar vacio")])
    telefono = TelField("Telefono", validators=[InputRequired("Este campo no puede estar vacio")])
    image = FileField("Imagen", validators=[FileAllowed(["jpeg", "jpg", "png"], "Solo imagenes")])
    submit = SubmitField("Agregar usuario")
    
class CrearRetroalimentacion(FlaskForm):
    retroalimentacion = TextAreaField("Comentarios:", validators=[InputRequired("Este campo no puede estar vacio")] )
    puntaje = HiddenField("Puntaje:", validators=[InputRequired("Este campo no puede estar vacio")])
    retroalimentaciones = SelectField("Retroalimentaciones", coerce=int) 
    submit = SubmitField("Generar Retroalimentacion")