from flask import Flask, render_template
#from flaskext.mysql import MySQLimport urllib
from flaskext.mysql import MySQL
#from app import app
#from db_setup import init_db, db_session
from searchoptions import MusicSearchForm
from flask import flash, render_template, request, redirect
#from models import Album



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


	# cursor.execute("SELECT emp_no, first_name, last_name FROM employees limit 3;")
 #    data = cursor.fetchall()
 #    print(type(data))
 #    return str(data[0])


# @app.route('/test1')
# def test_ui():
#     contents = urllib.urlopen("http://127.0.0.1:5000/test_get_db").read()
#     return render_template('index.html')
@app.route('/SearchBar')
def getsearch_bar():
	return render_template("searchbar.html")

 
 
@app.route('/', methods=['GET', 'POST'])
def index():
    search = MusicSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
 
    return render_template('searchbar.html', form=search)
 
 
@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
 
    if search.data['search'] == '':
        qry = db_session.query(Album)
        results = qry.all()
 
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        return render_template('results.html', results=results)


@app.route('/linkMe')
def get_linkme():
    return 'LinkMe is Active!'

@app.route('/JenkinsTest')
def get_jenkinspage():
    return 'Jenkins Status: UP!'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=False)
