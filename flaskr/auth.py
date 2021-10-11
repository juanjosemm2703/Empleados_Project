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
    if form.is_submitted():
        correo = form.correo.data
        password = form.password.data
        error = None
        user = Usuario.query.filter_by(correo=correo).first()


        if user is None:
            error = "Correo electronico incorrecto."


        elif not user.password == password:
            error = "Contrasena incorrecta."


        if error is None:
            login_user(user)
            next = request.args.get('next')
            if next:
                if not is_safe_url(next, {urlparse(request.base_url).netloc }):
                    return abort(400)
            return redirect(next or url_for('system.view'))
        flash(error)

    return render_template("auth/login.html", form=form)




@bp.route("/forgot_password", methods=("GET", "POST"))
def ForgotPassword():
    """Olvido la contrasena"""
    if request.method == "POST":
        try:
            print("Se envio correo")
            return redirect(url_for('login'))
        except ValueError as e:
            flash(str(e))
            return render_template('auth/ForgotPassword.html')

    return render_template("auth/ForgotPassword.html")


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
