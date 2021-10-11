import os

from flask import Flask
from flaskr.sqla import sqla
from flask_migrate import Migrate
from flaskr.login import login_manager



def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY=os.urandom(24),
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "Empleados.db"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/hello")
    def hello():
        return "Hello, World!"

    #Configuracion SQLAlchemy
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI=f'sqlite:///{app.config["DATABASE"]}',
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    sqla.init_app(app)

    #configure Flask-Migrate
    Migrate(app, sqla, render_as_batch=True)

    #configure Flask-Login
    # login_manager.init_app(app)

    # apply the blueprints to the app
    from flaskr import auth, system

    app.register_blueprint(auth.bp)
    app.register_blueprint(system.bp)

    # make url_for('index') == url_for('blog.index')
    # in another app, you might define a separate main index here with
    # app.route, while giving the blog blueprint a url_prefix, but for
    # the tutorial the blog will be the main index
    app.add_url_rule("/", endpoint="auth.login")

    return app