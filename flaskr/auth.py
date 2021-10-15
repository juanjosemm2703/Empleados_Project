from flask import abort, Blueprint, flash, redirect, render_template, request, session, url_for

from flask_login import login_user, current_user
from urllib.parse import urlparse
from is_safe_url import is_safe_url

from flaskr.forms import LogInForm

from flaskr.models import Usuario

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=("GET", "POST"))
def login():
    form = LogInForm()
    """Log in a registered user by adding the user id to the session."""
    if form.validate_on_submit():
        correo = form.correo.data
        password = form.password.data
        error = None
        user = Usuario.query.filter_by(correo=correo).first()

        if user is None:
            error = "Correo electrónico incorrecto."

        elif not user.correct_password(password):
            error = "Contrasena incorrecta."
        
        elif not user.estado:
            error = "Ingrese un correo y una clave válida"
        
        if error is None:
            login_user(user)
            next = request.args.get('next')
            if next:
                if not is_safe_url(next, {urlparse(request.base_url).netloc }):
                    return abort(400)
            return redirect(next or url_for('system.profile'))
        flash(error, "danger")

    return render_template("auth/login.html", form=form)


@bp.route("/forgot_password", methods=("GET", "POST"))
def ForgotPassword():
    """Olvido la contrasena"""
    try:
        if request.method == "POST":
            print("Se envio correo")
            flash("Te enviamos un correo con una contraseña temporal")
            return redirect(url_for('auth.login'))
    except ValueError as e:
            flash(str(e))
            return render_template('auth/ForgotPassword.html')

    return render_template("auth/ForgotPassword.html")



@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))

