import os

from flask import Flask
from flaskr.sqla import sqla
from flaskr.login import login_manager
from flaskr.mail import mail


def create_app(test_config=None):
    basedir = os.path.abspath(os.path.dirname(__file__))
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        #clave secreta
        # SECRET_KEY=os.environ['SECRET_KEY'],
        SECRET_KEY=os.urandom(24),
        # base de datos en la carpeta instance
        DATABASE=os.path.join(app.instance_path, "Empleados.sqlite")
    )
    
    #configuracion de imagenes
    app.config.from_mapping(
        #Solo archivos de imagen
        ALLOWED_IMAGE_EXTENSIONS = ["jpeg", "jpg", "png"],
        #tamano maximo
        MAX_CONTENT_LENGTH = 16 * 1024 * 1024,
        #carga de fotos
        IMAGE_UPLOADS = os.path.join(basedir, "static/img")
    )

    if test_config is None:
        # carga la config.py si no hay configuracion de testeo
        app.config.from_pyfile("config.py", silent=True)
    else:
        # carga la configuracion de testeo
        app.config.update(test_config)

    # crea la carpeta unstance si no existe
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #Configuracion SQLAlchemy
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI=f'sqlite:///{app.config["DATABASE"]}',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    sqla.init_app(app)

    #configurando Flask-Login
    login_manager.init_app(app)

    # Aplicando los blueprint
    from flaskr import auth, system

    app.register_blueprint(auth.bp)
    app.register_blueprint(system.bp)

    #redirigiendo la ruta "/" a auth.login
    app.add_url_rule("/", endpoint="auth.login")
    
    # Servidor de correo:
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587 # Puerto 587 para TLS // Puerto 465 para SSL
    app.config['MAIL_USE_TLS'] = True
    app.config.from_pyfile('mail.cfg')
    
    mail.init_app(app)

    return app