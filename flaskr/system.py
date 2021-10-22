import functools
from flask import jsonify
import json
import os, datetime
from flask import  Blueprint, send_from_directory, flash, redirect, render_template, request,  url_for, current_app
from flask import flash
from secrets import token_hex
from datetime import datetime as dt

from werkzeug.utils import secure_filename 
from flaskr.models import Usuario, Retroalimentacion, Rol
from flaskr.forms import FilterForm, NewUserForm, CrearRetroalimentacion
from flask_login import login_required
from flask_login import current_user
from flask_wtf.file import FileRequired

from flaskr.forms import ChangePassword
from flaskr.sqla import sqla

from sqlalchemy import extract

from flask_mail import Message
from flaskr.mail import mail

import random

bp = Blueprint("system", __name__, url_prefix="/system")

# Password aleatorio de letras y números:
def generate_random_password():
    min = "abcdefghijklmnñopqrstuvwxyz"
    may = min.upper()
    nros = "0123456789"
    base = min + may + nros
    longitud = 8
    muestra = random.sample(base, longitud)
    pwd_random = "".join(muestra)
    return pwd_random

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
        
@bp.route("/uploads/<filename>")
def uploads(filename):
    return send_from_directory(current_app.config["IMAGE_UPLOADS"], filename)

@bp.route("/view/<int:usuario_id>")
@login_required
@admin_required
def view(usuario_id):
    usuario = Usuario.query.filter_by(idUsuario=usuario_id, estado=1).first()
    error = None
    if not usuario:
        error = "El usuario con este id no se cnuentra en la base de datos"
    if error is None:
        if usuario.idRol == 3:
            retroalimentaciones = Retroalimentacion.query.filter_by(idEmpleado=usuario.idUsuario).order_by(Retroalimentacion.fecha.desc()).limit(5).all()
            return render_template('system/view.html',usuario=usuario, retroalimentaciones=retroalimentaciones)    
        return render_template('system/view.html',usuario=usuario)
    flash(error, "danger")
    return redirect(url_for("system.table"))
    

@bp.route("/delete/<int:usuario_id>")
@login_required
@admin_required
def delete(usuario_id):
    error = None
    usuario = ""
    if current_user.idRol == 2:
        usuario = Usuario.query.filter_by(idUsuario=usuario_id, estado=1, idRol=3).first()
    elif current_user.idRol == 1:    
        usuario = Usuario.query.filter(Usuario.idUsuario == usuario_id, Usuario.estado == 1, (Usuario.idRol == 3) | (Usuario.idRol == 2)).first()

    if not usuario:
        error = "El usuario no se encuentra en la base de datos"
    
    if error is None:
        usuario.estado=0
        sqla.session.commit()
        flash("El usuario fue desactivado con exito", "success")
        return redirect(url_for("system.table"))
    flash(error, "danger")
    return redirect(url_for("system.table"))

@bp.route("/nuevacontraseña")
@login_required
def nueva_contrasena():
    return "Enviar un correo con una nueva contraseña"


@bp.route("/retroalimentacion/<int:usuario_id>", methods=("GET", "POST"))
@login_required
@admin_required
def retroalimentacion(usuario_id):
    error = None
    usuario = Usuario.query.filter_by(idUsuario=usuario_id, estado=1, idRol=3).first()

    if not usuario:
        error = "El usuario con este id no se encuentra en la base de datos o no se le puede genera una retroalimentacion"
        
    if error is None:
        form = CrearRetroalimentacion()
        retroalimentaciones = sqla.session.query(Retroalimentacion).join(Usuario,Usuario.idUsuario==Retroalimentacion.idEmpleado).filter_by(idUsuario=usuario_id).order_by(Retroalimentacion.fecha.desc()).limit(5).all()
        
        categorias = [(0, "---")]
        for r in retroalimentaciones:
          choice = (r.idRetroalimentacion, r.fecha.strftime("%Y-%m-%d"))
          categorias.append(choice) 
           
        form.retroalimentaciones.choices = categorias
            
        try:
            is_ajax = int(request.args["ajax"])
        except:
            is_ajax = 0
            

        if form.validate_on_submit():
            try:
                if int(form.retroalimentaciones.data) > 0:
                    nueva_retroalimentacion = Retroalimentacion.query.filter_by(idRetroalimentacion=int(form.retroalimentaciones.data)).first()
                    mensaje = "La retroalimentacion ha sido editada con exito"
                    
                elif int(form.retroalimentaciones.data) == 0:
                    nueva_retroalimentacion = Retroalimentacion()
                    mensaje = "La retroalimentacion ha sido creada con exito"
                nueva_retroalimentacion.idEmpleado = usuario.idUsuario
                nueva_retroalimentacion.idAdministrador = current_user.idUsuario
                nueva_retroalimentacion.comentario = form.retroalimentacion.data
                nueva_retroalimentacion.puntaje = form.puntaje.data
                nueva_retroalimentacion.fecha = datetime.datetime.utcnow()
                
                sqla.session.add(nueva_retroalimentacion)
                sqla.session.commit()
                category = "success"
                
            except Exception as e:
                print(e)
                mensaje = "No se pudo generar la retroalimentacion"
                category = "danger"
                
            flash(mensaje, category)
            return redirect(url_for('system.view', usuario_id=usuario_id))
        
        if is_ajax:
           
            retroalimentacion = Retroalimentacion.query.filter_by(idRetroalimentacion=int(request.args["id"]),idEmpleado=usuario_id).first()
            retroalimentacion = Retroalimentacion.query.filter_by(idRetroalimentacion=int(request.args["id"]),idEmpleado=usuario_id).first()
            if not retroalimentacion:
                retroalimentacion = { "comentario": "", "puntaje": "0"}
                retroalimentacion = json.dumps(retroalimentacion)
                return retroalimentacion
            else:
                retroalimentacion = { "comentario": retroalimentacion.comentario, "puntaje": retroalimentacion.puntaje}
                retroalimentacion = json.dumps(retroalimentacion)
                return retroalimentacion
        
        return render_template('system/retroalimentacion.html', form=form, usuario=usuario, retroalimentaciones=retroalimentaciones)
    flash(error, "danger")
    return redirect(url_for('system.table'))   

@bp.route("/dashboard")
@login_required
@admin_required
def dashboard():
    usuarios= Usuario.query.filter_by(idRol=3,estado=1).all()
    CantEmpleado= len(usuarios)

    admin= Usuario.query.filter_by(idRol=2,estado=1).all()
    CantAdm= len(admin)

    Pun = Retroalimentacion.query.filter_by(idEmpleado=2).all()
    sum=0
    for i in Pun:
        sum= sum + i.puntaje
    Prom= sum/len(Pun)
    
    Retro = Retroalimentacion.query.filter(extract('month', Retroalimentacion.fecha) == dt.today().month,
                                extract('year', Retroalimentacion.fecha) == dt.today().year,
                                extract('day', Retroalimentacion.fecha) >= 1).all()
                        
    CantRetro= len(Retro)
    return render_template('system/index.html',CantEmple=CantEmpleado,CantAdmi=CantAdm,PromPunt=Prom,CantR=CantRetro)


@bp.route("/table")
@login_required
@admin_required
def table():
    form = FilterForm(request.args, meta={"csrf": False})
     
    if current_user.idRol == 1:
        usuarios = Usuario.query.filter((Usuario.idRol == 3) | (Usuario.idRol == 2), Usuario.estado == 1).all()
    elif current_user.idRol == 2:
        usuarios = Usuario.query.filter_by(idRol = 3, estado=1).all()

    
    
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
    
    opciones = usuarios_mostrar(10,1)    
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
            flash("La contraseña ha sido editada exitosamente", "success")
            return render_template('system/profile.html', form=form)
        else:
            flash(error, "danger")

    if current_user.idRol == 3:
        retroalimentaciones = Retroalimentacion.query.filter_by(idEmpleado=current_user.idUsuario).order_by(Retroalimentacion.fecha.desc()).all()
        return render_template('system/profile.html', retroalimentaciones=retroalimentaciones, form=form)
    return render_template('system/profile.html', form=form)


@bp.route("/edit/<int:usuario_id>", methods=("GET", "POST"))
@login_required
@admin_required
def edit(usuario_id):
    error = None
    usuario = Usuario.query.filter_by(idUsuario=usuario_id, estado=1).first()
    if not usuario:
        error = "El usuario con este id no se encuentra en la base de datos"
    if error is None:
        
        form = NewUserForm()
        categorias =[]
        for i in range(current_user.idRol, 3):
            rol = Rol.query.filter_by(idRol=i+1).first()
            rol_choice = (rol.idRol, rol)
            categorias.append(rol_choice)

        form.idRol.choices = categorias

        if form.validate_on_submit():
            
            filename = usuario.image
            try:
                if form.image.data:
                    filename = save_image_upload(form.image)
                
                if usuario.correo != form.correo.data:    
                    usuario.correo = form.correo.data
                if usuario.cedula != form.cedula.data: 
                    usuario.cedula = int(form.cedula.data)
                usuario.nombre = form.nombre.data
                usuario.apellido = form.apellido.data
                usuario.fecha_ingreso = form.fecha_ingreso.data
                usuario.fecha_contrato = form.fecha_contrato.data
                usuario.tipo_contrato = form.tipo_contrato.data
                usuario.cargo = form.cargo.data
                usuario.dependencia = form.dependencia.data
                usuario.salario = float(form.salario.data)
                usuario.idRol = int(form.idRol.data)
                usuario.direccion = form.direccion.data
                usuario.celular = int(form.celular.data)  
                usuario.telefono = int(form.telefono.data)
                usuario.image = filename
                sqla.session.commit()
                flash("El usuario fue editado con exito", "success")
                return redirect(url_for('system.view',usuario_id=usuario_id))
            except ValueError as e:
                flash(str(e), "danger")
                return redirect(url_for('system.table'))
            
        form.correo.data = usuario.correo
        form.nombre.data = usuario.nombre
        form.apellido.data = usuario.apellido
        form.cedula.data = usuario.cedula
        form.fecha_ingreso.data = usuario.fecha_ingreso
        form.fecha_contrato.data = usuario.fecha_contrato
        form.tipo_contrato.data = usuario.tipo_contrato
        form.cargo.data = usuario.cargo
        form.dependencia.data = usuario.dependencia
        form.salario.data = usuario.salario
        form.idRol.data = usuario.idRol
        form.direccion.data = usuario.direccion
        form.celular.data = usuario.celular
        form.telefono.data = usuario.telefono  
        return render_template('system/edit.html',usuario=usuario, form=form)
    
    flash(error, "danger")
    return redirect(url_for('system.table'))


@bp.route("/newuser", methods=['POST', 'GET'])
@login_required
@admin_required
def NewUser():
    form = NewUserForm() 
    categorias =[]
    
    for i in range(current_user.idRol, 3):
        rol = Rol.query.filter_by(idRol=i+1).first()
        rol_choice = (rol.idRol, rol)
        categorias.append(rol_choice)
    
    form.idRol.choices = categorias
    
    if form.validate_on_submit() and form.image.validate(form, extra_validators=(FileRequired("Este campo no puede estar vacio"),)):
        user = Usuario.query.filter((Usuario.correo==form.correo.data) | (Usuario.cedula==form.cedula.data)).first()
        if user:
            error = "Ya existe un usuario con estos datos"
        else:
            filename = save_image_upload(form.image)
            
            pwd_random = generate_random_password()
                        
            nuevo_usuario = Usuario(
                correo = form.correo.data,
                password  = pwd_random,
                nombre = form.nombre.data,
                apellido = form.apellido.data,
                cedula = int(form.cedula.data),
                fecha_ingreso = form.fecha_ingreso.data,
                fecha_contrato = form.fecha_contrato.data,
                tipo_contrato = form.tipo_contrato.data,
                cargo = form.cargo.data,
                dependencia = form.dependencia.data,
                salario = float(form.salario.data),
                idRol = int(form.idRol.data),
                direccion = form.direccion.data,
                celular = int(form.celular.data),  
                telefono = int(form.telefono.data),
                image = filename,
            )
            sqla.session.add(nuevo_usuario)
            sqla.session.commit()
            
            nombre = form.nombre.data
            usuario = form.correo.data
            password = pwd_random
            msg = Message('USUARIO ACTIVO', sender='empleados.project@gmail.com', recipients=[form.correo.data])
            msg.html = render_template('email_new_user.html', nombre=nombre, usuario=usuario, password=password)
            mail.send(msg)
            flash("Usuario creado con exito","success")
            return redirect(url_for('system.table'))
        flash(error, "danger")
    return render_template('system/NewUser.html',form=form)

def save_image_upload(image):
    # Creando un nombre de archivo unico para imagenes
    format = "%Y%m%dT%H%M%S"
    now = datetime.datetime.utcnow().strftime(format)
    random_string = token_hex(2)
    filename = random_string + "_" + now + "_" + image.data.filename
    filename = secure_filename(filename)
    image.data.save(os.path.join(current_app.config["IMAGE_UPLOADS"], filename))
    return filename
