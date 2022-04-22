from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)

# Change this to your secret key (can be anything, it's for extra protection)
app.secret_key = '12345678'

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Amira.13516143'
app.config['MYSQL_DB'] = 'swe'

# Intialize MySQL
mysql = MySQL(app)
userID = ''


@app.route('/')
def landing():
    return render_template("index.html")


@app.route('/library/')
def library():
    return render_template("library.html")


@app.route('/login/', methods=['GET', 'POST'])
def login():
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'txtEmail' in request.form and 'txtPassword' in request.form:
        # Create variables for easy access
        email = request.form['txtEmail']
        password = request.form['txtPassword']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s;', (email, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        cursor.close()
        print(account)
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['User_ID'] = account['User_ID']
            session['Username'] = account['Username']
            session['type'] = account['type']
            # Redirect to home page
            return redirect(url_for('homePage'))

    # Show the login form with message (if any)
    return render_template('login.html')


@app.route('/sigupPage/')
def signupPage():
    return render_template('signup.html')


@app.route('/profile/', methods=['GET'])
def profile():
    username = ''
    fname = ''
    lname = ''
    email = ''
    dept = ''
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'GET':
        cursor.execute('SELECT * FROM users WHERE User_ID = %s', (session['User_ID']))
        # Fetch one record and return result
        account = cursor.fetchone()
        fname = account['first_name']
        lname = account['last_name']
        username = account['Username']
        email = account['email']
        dept = account['department']
    cursor.close()
    return render_template('public.html', username=username, fname=fname, lname=lname, email=email, dept=dept)


@app.route('/loginpage/')
def loginPage():
    return render_template('login.html')


@app.route('/homepage/')
def homePage():
    if session['type'] == '0':  # student
        return render_template('Home.html')
    else:  # admin
        return render_template('Adminfeed.html')


@app.route('/UserSettingsPage/', methods=['POST', 'GET'])
def userSettingsPage():
    username = ''
    fname = ''
    lname = ''
    email = ''
    dept = ''
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'GET':
        cursor.execute('SELECT * FROM users WHERE User_ID = %s', (session['User_ID']))
        # Fetch one record and return result
        account = cursor.fetchone()
        fname = account['first_name']
        lname = account['last_name']
        username = account['Username']
        email = account['email']
        dept = account['department']

    if request.method == 'POST' and request.form['pass'] == request.form['confirmpass']:
        fname = request.form['fname']
        lname = request.form['lname']
        username = request.form['username']
        email = request.form['email']
        dept = request.form['dept']
        if 'pass' in request.form:
            cursor.execute(
                'UPDATE users set first_name = %s, last_name = %s, department = %s, password = %s, email = %s, Username = %s WHERE User_ID = %s',
                (fname, lname, dept, [request.form['pass']],
                 email, username, [session['User_ID']],))
            mysql.connection.commit()
        else:
            cursor.execute(
                'UPDATE users set first_name = %s, last_name = %s, department = %s, email = %s, Username = %s WHERE User_ID = %s',
                (fname, lname, dept, email, username, [session['User_ID']],))
            mysql.connection.commit()

    cursor.close()
    return render_template('settings-user.html', username=username, fname=fname, lname=lname, email=email, dept=dept)


if __name__ == '__main__':
    app.run()
