from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_message = "Por favor ingrese su usuario y contraseña"
login_manager.login_message_category = "danger"
login_manager.login_view = "auth.login" 