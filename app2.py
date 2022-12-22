#!/usr/bin/python3
from flask import Flask, make_response, request, render_template
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

try:
    FLAG = open("./flag.txt", "r").read()
except:
    FLAG = "[**FLAG**]"

@app.route('/')
def index():
    if request.method == "GET":
        flag = request.cookies.get("christmasCookie")
        if(flag):
            return render_template('flag.html')
        else:
            return render_template('index.html')

@app.route("/setcookie", methods=["GET", "POST"])
def setcookie():
    if request.method == "POST":
        res = make_response("Create Cookie!!")
        res.set_cookie("christmasCookie", FLAG)
        return res

app.run(host="0.0.0.0", port=8000)