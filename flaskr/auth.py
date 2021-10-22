from flask import abort, Blueprint, flash, redirect, render_template, request, session, url_for
from flask_login import login_user, current_user
from urllib.parse import urlparse
from is_safe_url import is_safe_url
from flask_mail import Message
from flaskr.mail import mail
from flaskr.forms import LogInForm, ForgotPasswordForm
from flaskr.models import Usuario
from flaskr.sqla import sqla
from flaskr.system import generate_random_password


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
            error = "Usuario incorrecto."

        elif not user.correct_password(password):
            error = "Contraseña incorrecta."
        
        elif not user.estado:
            error = "Ingrese un usuario y una contraseña válida."
        
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
    form = ForgotPasswordForm()
    """Olvidó la contrasena"""
    if form.validate_on_submit():
        email = form.email.data
                
        password = generate_random_password()
        error = None
        user = Usuario.query.filter_by(correo=email).first()
        
        if user is None:
            error = "Correo electrónico incorrecto."
            
        if error is None:
            user.password = password
            sqla.session.commit()
            msg = Message('RESTABLECER CONTRASEÑA', sender='empleados.project@gmail.com', recipients=[email])
            msg.html = render_template('email_password.html', password=password)
            mail.send(msg)
            flash("Te enviamos un email con una contraseña temporal.", "info")
            return redirect(url_for('auth.login'))
        flash(error, "danger")
        
    return render_template('auth/ForgotPassword.html', form=form)

@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))
