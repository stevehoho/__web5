from flask import Flask ,render_template

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1> hello world </h1>"

@app.route("/bootstrap")
def bootstrap():
    name = "Steve"
    chinese = 89
    english = 95
    math = 72
    return render_template("index.html", name=name, chinese=chinese, english=english, math=math)
