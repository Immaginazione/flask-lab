from flask import Flask
from flask import url_for
from flask import render_template
from markupsafe import escape


app = Flask(__name__)

@app.route("/")
def home():
    studenti = [{"href":"#","name":"Egle"},
                {"href":"#","name":"Dario"}]
    return render_template("home.html", students=studenti,
                            nome_materia="python")
    # return f"Benvenuto<a href='{url_for('about_me')}'>back</a>"

@app.route("/about_me")
def about_me():
    return f"<p>Ciao sono Mattia e mi piace Flask</p><a href='{url_for('home')}'>back</a>"