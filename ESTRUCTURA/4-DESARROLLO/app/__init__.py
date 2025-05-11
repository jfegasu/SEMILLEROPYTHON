from flask import Flask
from playhouse.flask_utils import FlaskDB

# Configuración de Peewee
db_wrapper = FlaskDB()

def create_app(config_class='config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db_wrapper.init_app(app)

    # Importar y registrar blueprints
    from app.routes import main_bp
    app.register_blueprint(main_bp)

    return app
