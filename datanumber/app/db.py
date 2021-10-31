from app import app
from flaskext.mysql import MySQL
from config import ROOT_USER, ROOT_PASSWORD, DATA_DB, DATABASE_HOST

mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = ROOT_USER
app.config['MYSQL_DATABASE_PASSWORD'] = ROOT_PASSWORD
app.config['MYSQL_DATABASE_DB'] = DATA_DB
app.config['MYSQL_DATABASE_HOST'] = DATABASE_HOST
mysql.init_app(app)
