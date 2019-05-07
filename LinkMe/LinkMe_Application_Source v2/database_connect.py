import mysql.connector
from wtforms import Form, StringField, SelectField, TextField, TextAreaField, SubmitField, validators, ValidationError
import smtplib



mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="cmpe",
        database="employees"
    )
cursor = mydb.cursor()

class Employee:
    
    def __init__(self, emp_no, first_name, last_name, hire_date):
        self.emp_no = emp_no
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date

    def get_name(self):
        return str(self.first_name) + " " + str(self.last_name)


class EmployeeSearchForm(Form):
    choices = [('first_name', 'First Name'),
               ('emp_no', 'Employee Number')]
    select = SelectField('Search for search:', choices=choices)
    search = StringField('')


class ContactForm(Form):
    name = StringField("Name")
    email = StringField("Email")
    subject = StringField("Subject")
    message = TextAreaField("Message")
    #submit = SubmitField("Send")


def get_db_data(index_a):
    employees = []
    cursor.execute("SELECT emp_no, first_name, last_name, hire_date FROM employees limit {}, {};".format(str(index_a), str(500)))
    data = cursor.fetchall()
    for people in data:
        employees.append(Employee(str(people[0]), str(people[1]), str(people[2]), str(people[3])))
    print(len(employees))
    return employees



def sql_query(search_string, filter):
    employees = []
    cursor.execute("SELECT emp_no, first_name, last_name, hire_date FROM employees WHERE {} LIKE '{}%' limit 5;".format(filter, search_string))
    data = cursor.fetchall()
    for people in data:
        employees.append(Employee(str(people[0]), str(people[1]), str(people[2]), str(people[3])))

    return employees


def send_mail(to_mail, subject, message):

    gmail_user = 'link.me.connect@gmail.com'
    gmail_password = 'mlink#22'

    sent_from = gmail_user
    to = [str(to_mail)]
    SUBJECT = str(subject)
    TEXT = str(message)

    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, message)
        server.close()
    except:
        print("Something Went Wrong!")


