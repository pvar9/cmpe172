from flask import Flask, render_template
#from flaskext.mysql import MySQLimport urllib


app = Flask(__name__)


# @app.route('/test_get_db')
# def test_getDB():
#     mysql = MySQL()
#     app.config['MYSQL_DATABASE_USER'] = 'root'
#     app.config['MYSQL_DATABASE_PASSWORD'] = 'pass123'
#     app.config['MYSQL_DATABASE_DB'] = 'employees'
#     app.config['MYSQL_DATABASE_HOST'] = 'localhost'
#     mysql.init_app(app)

#     conn = mysql.connect()
#     cursor = conn.cursor()

#     cursor.execute("SELECT first_name, last_name FROM employees limit 2;")
#     data = cursor.fetchall()
#     print(type(data))
#     return str(data)


# @app.route('/test1')
# def test_ui():
#     contents = urllib.urlopen("http://127.0.0.1:5000/test_get_db").read()
#     return render_template('index.html')

@app.route('/linkMe')
def get_linkme():
    return 'LinkMe is Active!'

@app.route('/JenkinsTest')
def get_jenkinspage():
    return 'Jenkins Status: UP'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False)
