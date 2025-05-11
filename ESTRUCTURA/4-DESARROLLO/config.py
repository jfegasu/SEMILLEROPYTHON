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

    DATABASE=SQLITE


    



