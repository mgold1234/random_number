import random
from flask import jsonify, Flask
from config import ROOT_USER, ROOT_PASSWORD, DATA_DB, DATABASE_HOST, DATABASE_PORT
import pymysql.cursors

app = Flask(__name__)


@app.route('/')
def numbers():
    conn = pymysql.connect(host=DATABASE_HOST, port=DATABASE_PORT, user=ROOT_USER,passwd = ROOT_PASSWORD, db=DATA_DB)

    cursor = conn.cursor()

    try:

        j = random.randrange(1, 100)
        sql = "INSERT INTO number(random_number) VALUES(%s)"

        cursor.execute(sql, (j))
        cursor.execute("SELECT * from number")
        rows = cursor.fetchall()

        resp = jsonify(rows)
        return resp

    except pymysql.connect.Error as err:
        print("Something went wrong: {}".format(err))
        return resp.status_code, 500

    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)