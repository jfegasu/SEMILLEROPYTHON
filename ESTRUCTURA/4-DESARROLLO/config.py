import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave_secreta')

    # Configuración de la base de datos para Peewee
    SQLITE = {
        'name': os.path.join(BASE_DIR, 'app.db'),
        'engine': 'peewee.SqliteDatabase',
    }
    DATABASE=SQLITE



