from flask import Flask   #, url_for
from flask import request #載入 Request 物件
from flask import redirect # 載入 redirect 函式
from flask import render_template # 載入 render_template 函式
from flask import session
import mysql.connector

app = Flask(__name__,) 
app.secret_key="celesteSecret" # 設定 Session 密鑰：可以填寫任何字串但不告訴別人

# 連接 MySQL/MariaDB 資料庫
mydb = mysql.connector.connect(
    host = "127.0.0.1",      # 主機名稱
    # database="website",      # 資料庫名稱
    user = "root",           # 帳號
    password = "0117"        # 密碼
)
print(mydb)
cursor = mydb.cursor()
# result=[]

# # Show db
# cursor.execute("SHOW DATABASES")
# for x in cursor:
#     print(x)

# SQL 查詢語句
def sqlQueryAll(sql):
    cursor.execute("USE website")
    # sql: str # = "SELECT * FROM member"
    try:
        # 執行SQL語句
        cursor.execute(sql)
        # 獲取所有記錄列表 fetchone / fetchall
        # results = cursor.fetchone() #fetchone只獲取一條資料， 返回元組型別資料
        # print(results)
        result = cursor.fetchall()    #fetchall返回查詢的全部資料， 返回元組型別資料
        print(result)
        return result
    except:
        print("Error: unable to fetch data")
        return False


@app.route("/")
def index():
    # session["status"] = "未登入"

    # 重新跑一次資料
    # cursor.execute(sql)
    # result = cursor.fetchall()    #fetchall返回查詢的全部資料， 返回元組型別資料
    # # print(result)
    sqlQueryAll("SELECT * FROM member")

    return render_template("index.html")


@app.route("/signup", methods=["POST"])
def signup():
    newName = request.form["newName"]
    newAccount = request.form["newAccount"]
    newPassword = request.form["newPassword"]

    # 重複註冊
    if sqlQueryAll("SELECT * FROM member") != False:
        for x in sqlQueryAll("SELECT * FROM member"):
            if newAccount == x[2]:
                return redirect("/error/?message=帳號已被註冊")

    # 成功註冊
    sql = "INSERT INTO member(name, username, password) VALUES(%s, %s, %s)"
    val = (newName, newAccount, newPassword)
    cursor.execute(sql, val)
    mydb.commit()
    print(cursor.rowcount, "新增資料成功")
    return redirect("/")


@app.route("/signin", methods=["POST"])
def signin():
    account = request.form["account"]
    password = request.form["password"]
    
    # sqlQueryAll("SELECT * FROM member")
    # 登入成功
    if sqlQueryAll("SELECT * FROM member") != False:
        for x in sqlQueryAll("SELECT * FROM member"):
            if account == x[2] and password == x[3]:
                session["status"] = "已登入"
                session["name"] = str(x[1])
                return redirect("/member")
    # 登入失敗
    if(account == "" or password == ""):
        return redirect("/error/?message=請輸入帳號、密碼")
    else:
        return redirect("/error/?message=帳號、或密碼輸入錯誤")

@app.route("/member")
def member():
    if session["status"] == "未登入":
        return redirect("/")
    else:
        name = session["name"]
        return render_template("member.html", name = str(name))

@app.route("/error/")
def error():
    msg = request.args.get("message","自訂的錯誤訊息")
    # return render_template("error.html")
    # return msg
    return render_template("error.html",errorMessages = str(msg))

@app.route("/signout")
def signout():
    session["status"] = "未登入"
    session["name"] = "未登入"
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

# 關閉資料庫連線
mydb.close()