import random
import pymysql
from flask import Flask, jsonify
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'random_values'
app.config['MYSQL_DATABASE_HOST'] = 'db'
mysql.init_app(app)


@app.route('/')
def numbers():

    conn = mysql.connect()

    cursor = conn.cursor(pymysql.cursors.DictCursor)

    j = random.randrange(1, 100)
    sql = "INSERT INTO number(rnd_value) VALUES (%s)"

    cursor.execute(sql, (j))
    rows = cursor.fetchall()

    resp = jsonify(rows)
    resp.status_code = 200

    return resp


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')