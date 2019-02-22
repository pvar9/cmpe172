from flask import Flask, render_template
from flaskext.mysql import MySQLimport urllib2


app = Flask(__name__)


@app.route('/test_get_db')
def test_getDB():
    mysql = MySQL()
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'pass123'
    app.config['MYSQL_DATABASE_DB'] = 'employees'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(app)

    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.execute("SELECT first_name, last_name FROM employees limit 2;")
    data = cursor.fetchall()
    print(type(data))
    return str(data)


@app.route('/')
def test_ui():
    contents = urllib2.urlopen("http://127.0.0.1:5000/test_get_db").read()
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
