import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave_secreta')

    # Configuración de la base de datos para Peewee
    SQLITE = {
        'name': os.path.join(BASE_DIR, 'app.db'),
        'engine': 'peewee.SqliteDatabase',
    }
    #  Configuración de la base de datos MySQL para Peewee
    # pip install pymysql
    MYSQL = {
        'engine': 'peewee.MySQLDatabase',
        'name': 'nombre_base',
        'user': 'usuario',
        'password': 'contraseña',
        'host': 'localhost',
        'port': 3306,
        'charset': 'utf8mb4'
    }
    # pip install psycopg2-binary

    POSTGRES = {
        'engine': 'peewee.PostgresqlDatabase',
        'name': 'nombre_de_la_base',
        'user': 'usuario',
        'password': 'contraseña',
        'host': 'localhost',
        'port': 5432
    }
    # pip install pyodbc
    # Peewee no tiene un conector oficial específico para SQL Server, pero puedes usar playhouse.mssql_ext (extensiones no oficiales) o el conector genérico con ODBC.
    # 'dsn': 'Driver={ODBC Driver 17 for SQL Server};Server=localhost;Database=NombreDeBase;UID=usuario;PWD=contraseña;'

    SQLSERVER = {
        'engine': 'playhouse.mssql_ext.MSSQLDatabase',
        'name': 'NombreDeBase',
        'user': 'tu_usuario',
        'password': 'tu_contraseña',
        'host': 'localhost',
        'port': 1433,
        'driver': 'ODBC Driver 17 for SQL Server',
        'options': {
            'timeout': 10
        }
    }
    # pip install pyodbc

    ORACLE = {
        'engine': 'peewee.Database',  # Se sobrescribirá con una instancia directa
        'dsn': 'Driver={Oracle in instantclient_19_8};DBQ=localhost:1521/XEPDB1;UID=usuario;PWD=contraseña;'
    }

    DATABASE=SQLITE
# __init__.py con conexión manual
# from flask import Flask
# import pyodbc
# from peewee import Database
# from playhouse.flask_utils import FlaskDB
# from peewee import Model

# db_wrapper = FlaskDB()

# def create_app(config_class='config.Config'):
#     app = Flask(__name__)
#     app.config.from_object(config_class)

#     # Crear conexión manual
#     dsn = app.config['DATABASE']['dsn']
#     conn = pyodbc.connect(dsn)
#     database = Database(conn)

#     db_wrapper.init_app(app, database_override=database)

#     from app.routes import main_bp
#     app.register_blueprint(main_bp)

#     return app



    



