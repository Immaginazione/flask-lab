from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
#import json

app = Flask(__name__)
obj = {'subs':['orsociro@gmail.com','mattia.folcarelli@gmail.com','ernesto@gmail.com']}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sub", methods=['GET'])
def index_subs():
    # return json.dumps();
    return jsonify(obj)

@app.route("/sub/<id>", methods=['GET'])
def show_subs(id):
    return jsonify(obj['subs'][int(id)])

@app.route("/sub", methods=['POST'])
def create_subs():
    newSub = request.form['sub']
    obj['subs'].append(newSub)
    return jsonify({'data':newSub})