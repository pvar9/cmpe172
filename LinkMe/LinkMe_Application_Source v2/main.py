from flask import Flask, render_template, url_for, redirect, flash, request
from flask_oidc import OpenIDConnect

import database_connect

app = Flask(__name__)
app.config.update({
    'SECRET_KEY': 'SomethingNotEntirelySecret',
    'OIDC_CLIENT_SECRETS': './client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_SCOPES': ["openid", "profile", "email"],
    'OIDC_CALLBACK_ROUTE': '/authorization-code/callback', 
})

oidc = OpenIDConnect(app)

load_data = False
data = []
count = 1

@app.route("/", methods=['GET', 'POST'])
def home():
    global load_data
    global data

    search = database_connect.EmployeeSearchForm(request.form)
    more_results = request.form
    if request.method == 'POST':
        if 'search' in request.form:
            load_data = False
            return search_results(search)
        if 'more' in request.form:
            return search_results(search)
        if 'Email' in request.form:
            print("Sending Email....")
            return redirect(url_for('contact'))
    else:
        return render_template("home.html", oidc=oidc, form=search)


@app.route('/results', methods=['GET', 'POST'])
def search_results(search):
    global count
    global load_data
    if load_data:
        count = count + 500
        print(count)
        results = database_connect.get_db_data(count)
        return render_template('results.html', results=results, oidc=oidc, data=data, form=search)

    else:
        search_string = search.data['search']
        filter = search.data['select']
        print(search)
        print(search.data)

        if search_string == '':
            load_data = True
            count = 0
            results = database_connect.get_db_data(count)
            print("Getting All DB..")
        else:
            # display results
            results = database_connect.sql_query(search_string, filter)

        if not results:
            print('No results found!')
            flash('No results found!')
            return redirect('/')
        else:
            return render_template('results.html', results=results, oidc=oidc, data=data, form=search)

@app.route("/login")
@oidc.require_login
def login():
    return redirect(url_for("profile"))


@app.route("/profile")
@oidc.require_login
def profile():
    emp_data = False
    info = oidc.user_getinfo(["sub", "name", "email", "groups"])
    print(info)
    for val in data:
        if val.get_name() == info['name']:
            emp_data = val
            break

    if emp_data == False:
        emp_data = database_connect.Employee('00000','First', 'Last', '01-01-1700')

    return render_template("profile.html", profile=info, oidc=oidc, emp_data=emp_data)


@app.route("/logout", methods=["POST"])
def logout():
    oidc.logout()
    return redirect(url_for("home"))


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = database_connect.ContactForm(request.form)
    form.message.data = "Hi! My Name is {}! I would love to connect with you and learn more about your role in the company.".format(form.name.data)

    if request.method == 'POST':
        return contact_send(form)

    elif request.method == 'GET':
        return render_template('contact.html', form=form, oidc=oidc)

@app.route('/contact_send', methods=['GET', 'POST'])
def contact_send(send):
    print(send)
    print(send.data['email'])
    print(send.subject)
    print(send.message)
    database_connect.send_mail(send.email.data, send.subject.data, send.message.data)
    return render_template('email_sent.html', oidc=oidc)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000, debug=True)
