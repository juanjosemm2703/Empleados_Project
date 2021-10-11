from flask import abort, Blueprint, flash, redirect, render_template, request, session, url_for


from flask_login import login_user, current_user
from urllib.parse import urlparse
from is_safe_url import is_safe_url

from werkzeug.security import check_password_hash

# from flaskr.models import User

from flaskr.sqla import sqla
from flaskr.forms import LogInForm

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/login", methods=("GET", "POST"))
def login():
    form = LogInForm()
    """Log in a registered user by adding the user id to the session."""
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
    return redirect(url_for('login'))
