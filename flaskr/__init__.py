import os

from flask import Flask
from flaskr.sqla import sqla
from flask_migrate import Migrate
from flaskr.login import login_manager



def create_app(test_config=None):
    """Creando y configurando la aplicacion Flask."""
    """directorio base"""
    basedir = os.path.abspath(os.path.dirname(__file__))
    app = Flask(__name__, instance_relative_config=True)
    
    app.config.from_mapping(
        #clave secreta
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

    #configurando Flask-Migrate
    Migrate(app, sqla, render_as_batch=True)

    #configurando Flask-Login
    login_manager.init_app(app)

    # Aplicando los blueprint
    from flaskr import auth, system

    app.register_blueprint(auth.bp)
    app.register_blueprint(system.bp)

    #redirigiendo la ruta "/" a auth.login
    app.add_url_rule("/", endpoint="auth.login")

    return app