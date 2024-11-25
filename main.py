from flask import Flask
from time import sleep

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.route("/complicated")
def complicated():
    sleep(2.5)
    return "done"
