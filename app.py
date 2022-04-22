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


@app.route('/')
def landing():
    return render_template("index.html")


@app.route('/login/', methods=['GET', 'POST'])
def login():
    # Check if "username" and "password" POST requests exist (user submitted form)
    print("inside login")
    if request.method == 'POST' and 'txtEmail' in request.form and 'txtPassword' in request.form:
        # Create variables for easy access
        email = request.form['txtEmail']
        password = request.form['txtPassword']
        print("inside if")
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        print("connected to database")

        cursor.execute('SELECT * FROM users WHERE email = %s AND password = %s;', (email, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        print(account)
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['User_ID'] = account['User_ID']
            session['Username'] = account['Username']
            # Redirect to home page
            return render_template('Home.html')

    # Show the login form with message (if any)
    return render_template('login.html')


@app.route('/sigupPage/')
def signupPage():
    return render_template('signup.html')

@app.route('/loginpage/')
def loginPage():
    return render_template('login.html')

@app.route('/homepage/')
def homePage():
    return render_template('Home.html')

@app.route('/UserSettingsPage/')
def userSettingsPage():
    return render_template('settings-user.html')


if __name__ == '__main__':
    app.run()
