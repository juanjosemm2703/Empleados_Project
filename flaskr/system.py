import functools


from flask import abort, Blueprint, flash, redirect, render_template, request, session, url_for, current_app

from flaskr.forms import FilterForm
from flask_login import login_required
from flask_login import current_user

bp = Blueprint("system", __name__, url_prefix="/system")


def admin_required(view):
        @functools.wraps(view)
        def wrapped_view(**kwargs):
            if not current_user.idRol == 1:
                return redirect(url_for("system.view"))

            return view(**kwargs)

        return wrapped_view


@bp.route("/delete")
@login_required
def delete():
    return "Se elimina a la persona"


@bp.route("/nuevacontraseña")
@login_required
def nueva_contrasena():
    return "Enviar un correo con una nueva contraseña"


@bp.route("/retroalimentacion")
@login_required
def retroalimentacion():
    return render_template('system/retroalimentacion.html')


@bp.route("/dashboard")
@login_required
def dashboard():
    return render_template('system/index.html')


@bp.route("/table")
@login_required
def table():
    form = FilterForm(request.args, meta={"csrf": False})
    return render_template('system/table.html', form=form)


@bp.route("/profile")
@login_required
def profile():
    return render_template('system/profile.html')


@bp.route("/edit")
@login_required
def edit():
    return render_template('system/edit.html')



@bp.route("/view")
@login_required
def view():
    return render_template('system/view.html')



@bp.route("/newuser")
@login_required
@admin_required
def NewUser():
    # if not current_user.nombre == 1:
    #     return redirect(url_for('system.view'))
    return render_template('system/NewUser.html')






