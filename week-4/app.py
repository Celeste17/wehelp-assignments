from flask import Flask   #, url_for
from flask import request #載入 Request 物件
from flask import redirect # 載入 redirect 函式
from flask import render_template # 載入 render_template 函式
from flask import session

app = Flask(__name__,) 
app.secret_key="celesteSecret" # 設定 Session 密鑰：可以填寫任何字串但不告訴別人

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signin():
    account = request.form["account"]
    password = request.form["password"]
    # message ="唷唷唷唷"
    if account == "test" and password == "test":
        session["status"] = "已登入"
        return redirect("/member")
    elif(account == "" or password == ""):
        return redirect("/error/?message=請輸入帳號、密碼")
    else:
        return redirect("/error/?message=帳號、或密碼輸入錯誤")
    # else:
    # #     return redirect(url_for("error",message=message))
    #     return redirect("/error")

@app.route("/member")
def member():
    if session["status"] == "未登入":
        return redirect("/")
    else:
        return render_template("member.html")

@app.route("/error/")
def error():
    msg = request.args.get("message","自訂的錯誤訊息")
    # return render_template("error.html")
    # return msg
    return render_template("error.html",errorMessages = str(msg))

@app.route("/signout")
def signout():
    session["status"] = "未登入"
    return redirect("/")


# @app.route("/error/?message=請輸入帳號、密碼")
# def errorNull():
#     message="請輸入帳號、密碼"
#     return render_template("error.html", errorMessages=str(message))
# @app.route("/error/?message=帳號、或密碼輸入錯誤")
# def errorWrong():
#     message="帳號、或密碼輸入錯誤"
#     return render_template("error.html", errorMessages=str(message))


app.run(port=3000)