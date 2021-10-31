
from os import environ

ROOT_USER = environ.get("database_user")
ROOT_PASSWORD = environ.get("database_password")
DATA_DB = environ.get("database_db")
DATABASE_HOST = environ.get("service_host")
DATABASE_PORT = environ.get("service_port")