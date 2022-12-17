from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1> hello world </h1>"

@app.route("/bootstrap")
def bootstrap():
    return "<h1>Bootstrap</h1>"
