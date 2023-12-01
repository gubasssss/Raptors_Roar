from flask import Flask
from flask import render_template
app = Flask(__name__)
from flask import Flask, request, render_template, jsonify, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config.from_pyfile('config.py')

mysql = MySQL(app)

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('firstname')
    surname = request.form.get('lastname')
    email = request.form.get('email')
    comment = request.form.get('comment')
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO contato (name, surname, email, comment) VALUES (%s, %s, %s,%s)', (name, surname, email, comment))
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('contact'))

@app.route("/")
@app.route("/home.html")
def home():
    return render_template("home.html")

@app.route("/contact.html")
def contact():
    return render_template("contact.html")

@app.route("/about.html")
def about():
    return render_template("about.html")





