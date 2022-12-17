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
    context = {
        "title":"5G新時代",
        "banners":["一個城市的進步樣態，隨著經濟與科技發展而改變及演化;當5G網路結合聯網裝置，未來將產生眾多新創服務 改變城市面貌。",
        "透過5G智能物聯網，政府將能快速整合組織系統和服務，提昇資源運用的效率，透過最佳化都市管理和服 務，達到改善市⺠生活品質之目的。換言之，5G是實現 智慧城市的必要基礎。",
        "本研討會將透過實際案例分享，探討政府該如何透過手 機5G服務的結合應用，帶給⺠眾更多便利的服務，並為 城市帶來智慧新風貌。"]
    }
    return render_template("home.html",**context)

@app.route("/item1")
def item1():
    context = {
        "title":"何謂5G"
    }
    return render_template("item1.html",**context)

@app.route("/item2")
def item2():
    context = {
        "title":"醫療物聯網"
    }
    return render_template("item2.html",**context)

@app.route("/item3")
def item3():
    context = {
        "title":"智慧製造"
    }
    return render_template("item3.html",**context)