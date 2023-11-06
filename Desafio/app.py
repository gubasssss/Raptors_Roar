from flask import Flask
from flask import render_template
app = Flask(__name__)

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
