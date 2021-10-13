import functools
from flask import jsonify
import json

from flask import abort, Blueprint, flash, redirect, render_template, request, session, url_for, current_app

from flaskr.models import Usuario, Retroalimentacion, Rol
from flaskr.forms import FilterForm
from flask_login import login_required
from flask_login import current_user

from flaskr.forms import ChangePassword
from flaskr.sqla import sqla

bp = Blueprint("system", __name__, url_prefix="/system")


def admin_required(view):
        @functools.wraps(view)
        def wrapped_view(**kwargs):
            if current_user.idRol == 3:
                return redirect(url_for("system.profile"))

            return view(**kwargs)

        return wrapped_view


def contains_word(string1, string2):
    return (' ' + string1 + ' ') in (' ' + string2 + ' ')

def usuarios_mostrar(cant_opciones, rango):
    return [ i for i in range(rango,(cant_opciones*rango)+rango,rango)]
        

@bp.route("/view")
@login_required
@admin_required
def view():
    return render_template('system/view.html')


@bp.route("/delete")
@login_required
@admin_required
def delete():
    return "Se elimina a la persona"


@bp.route("/nuevacontraseña")
@login_required
def nueva_contrasena():
    return "Enviar un correo con una nueva contraseña"


@bp.route("/retroalimentacion")
@login_required
@admin_required
def retroalimentacion():
    return render_template('system/retroalimentacion.html')


@bp.route("/dashboard")
@login_required
@admin_required
def dashboard():
    return render_template('system/index.html')


@bp.route("/table")
@login_required
@admin_required
def table():
    form = FilterForm(request.args, meta={"csrf": False})
     
    if current_user.idRol == 1:
        usuarios = Usuario.query.filter((Usuario.idRol == 3) | (Usuario.idRol == 2)).all()
    elif current_user.idRol == 2:
        usuarios = Usuario.query.filter_by(idRol = 3).all()

    
    
    categorias = [(0, "---")]
    for i in range(current_user.idRol, 3):
        rol = Rol.query.filter_by(idRol=i+1).first()
        rol_choice = (rol.idRol, rol)
        categorias.append(rol_choice)

    form.rol.choices = categorias

    try:
        is_ajax = int(request.args["ajax"])
    except:
        is_ajax = 0

    if form.validate():
        
        if form.name.data.strip():
            usuarios = [usuario for usuario in usuarios if
                        contains_word(form.name.data.upper(), (usuario.nombre + ' ' + usuario.apellido).upper())]
            
            
        if form.rol.data:
            usuarios = [usuario for usuario in usuarios if usuario.idRol == int(form.rol.data)]
            
            
        if form.cargo.data.strip():
            usuarios = [usuario for usuario in usuarios if
                        contains_word(form.cargo.data.upper(), usuario.cargo.upper())]
            
        if form.dependencia.data.strip():
            usuarios = [usuario for usuario in usuarios if
                        contains_word(form.dependencia.data.upper(), usuario.dependencia.upper())]
            
        if form.date_admission.data:
            if form.date_admission.data == 1:
                usuarios = sorted(usuarios, key=lambda x: x.fecha_ingreso)
            if form.date_admission.data == 2:
                usuarios = sorted(usuarios, key=lambda x: x.fecha_ingreso, reverse=True)
            
            
    if is_ajax:
        if len(usuarios):
            total_usuarios = len(usuarios)
        else:
            total_usuarios = 0
        usuarios = [usuarios[i:i + int(request.args["cantidad"])] for i in range(0, len(usuarios), int(request.args["cantidad"]))]
        pagina = int(request.args["pagina"])
        
        if(len(usuarios)< pagina):
            usuarios = 0
            tabla_html = render_template("system/_filter_form.html", usuarios=usuarios)
            diccionario ={ "tabla": tabla_html, "total_usuarios": total_usuarios, 'usuarios_actuales': 0}
            return diccionario
        else:
            usuarios = usuarios[pagina-1]
            tabla_html = render_template("system/_filter_form.html", usuarios=usuarios)
            diccionario ={ "tabla": tabla_html, "total_usuarios": total_usuarios, 'usuarios_actuales': len(usuarios)}
            return diccionario
    
    opciones = usuarios_mostrar(4,2)    
    return render_template('system/table.html', form=form, usuarios=usuarios, opciones=opciones)


@bp.route("/profile", methods=("GET", "POST"))
@login_required
def profile():
    form = ChangePassword()

    if form.validate_on_submit():
        oldpassword = form.oldpassword.data
        password = form.password.data
        confirm = form.confirm.data
        error = None

        if not current_user.correct_password(oldpassword):
            error = "Contraseña incorrecta."

        if not password == confirm:
            error = "Las contraseñas no coinciden"

        if error is None:
            current_user.password = password
            sqla.session.commit()
        else:
            flash(error, "danger")

    if current_user.idRol == 3:
        retroalimentaciones = Retroalimentacion.query.filter_by(idEmpleado=current_user.idUsuario).order_by(Retroalimentacion.fecha.desc()).all()
        return render_template('system/profile.html', retroalimentaciones=retroalimentaciones, form=form)
    return render_template('system/profile.html', form=form)


@bp.route("/edit/")
@login_required
@admin_required
def edit():
    return render_template('system/edit.html')



@bp.route("/newuser")
@login_required
@admin_required
def NewUser():
    # if not current_user.nombre == 1:
    #     return redirect(url_for('system.view'))
    return render_template('system/NewUser.html')


