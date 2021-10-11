from flaskr import create_app
from flaskr.models import *
from flaskr.sqla import sqla

app = create_app()
app.app_context().push()
