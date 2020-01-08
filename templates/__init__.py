from flask import Flask
from .src.views import src_blueprint
from .build.views import build_blueprint

app = Flask(__name__)

# register the blueprints
app.register_blueprint(src_blueprint, url_prefix="/src")
app.register_blueprint(build_blueprint, url_prefix="/build")
