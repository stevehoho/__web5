from flask import Flask,render_template
import xlrd

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello! Flask!</h1>"


@app.route("/bootstrap")
def bootstrap():
    book = xlrd.open_workbook("static/others/student.xls")
    sh = book.sheet_by_index(0)
    #print(sh.cell_value(rowx=0, colx=1))
    student = {
        "name":sh.cell_value(rowx=0, colx=1),
        "chinese":sh.cell_value(rowx=1, colx=1),
        "english":sh.cell_value(rowx=2, colx=1),
        "math":sh.cell_value(rowx=3, colx=1)
    }    
    return render_template("index.html",**student)


@app.route("/home")
def home():
    return render_template("home.html", title="5g新時代")

@app.route("/item1")
def item1():
    return render_template("item1.html", title="何謂5g?")

@app.route("/item2")
def item2():
    return render_template("item2.html", title="醫療互聯網")

@app.route("/item3")
def item3():
    return render_template("item3.html", title="智慧製造")