from flask import abort, Blueprint, flash, redirect, render_template, request, session, url_for

from flask_login import login_user, current_user
from urllib.parse import urlparse
from is_safe_url import is_safe_url

from flaskr.sqla import sqla
from flaskr.forms import FilterForm

bp = Blueprint("system", __name__, url_prefix="/system")


@bp.route("/delete")
def delete():
    return ("Se elimina a la persona")


@bp.route("/nuevacontraseña")
def nueva_contrasena():
    return ("Enviar un correo con una nueva contraseña")


@bp.route("/retroalimentacion")
def retroalimentacion():
    return render_template('system/retroalimentacion.html')


@bp.route("/dashboard")
def dashboard():
    return render_template('system/index.html')


@bp.route("/table")
def table():
    form = FilterForm(request.args, meta={"csrf": False})
    return render_template('system/table.html', form=form)


@bp.route("/profile")
def profile():
    return render_template('system/profile.html')


@bp.route("/edit")
def edit():
    return render_template('system/edit.html')


@bp.route("/view")
def view():
    return render_template('view.html')


@bp.route("/newuser")
def NewUser():
    return render_template('NewUser.html')





