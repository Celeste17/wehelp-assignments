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
    database="website",      # 資料庫名稱
    user = "root",           # 帳號
    password = "0117"        # 密碼
)
print(mydb)
cursor = mydb.cursor()
# result=[]

# SQL 查詢語句(要用時再使用)
# def sqlQueryWebsite(sql):
#     # cursor.execute("USE website")
#     # sql: str = "SELECT * FROM member"
#     try:
#         # 執行SQL語句
#         cursor.execute(sql)
#         # 獲取所有記錄列表 fetchone / fetchall
#         # results = cursor.fetchone() #fetchone只獲取一條資料， 返回元組型別資料
#         # print(results)
#         result = cursor.fetchall()    #fetchall返回查詢的全部資料， 返回元組型別資料
#         print(result)
#         return result
#     except:
#         print("Error: unable to fetch data")
#         return False


@app.route("/")
def index():
    if session["name"] != False:
        return redirect("/member")
    return render_template("index.html")


@app.route("/signup", methods=["POST"])
def signup():
    newName = request.form["newName"]
    newAccount = request.form["newAccount"]
    newPassword = request.form["newPassword"]

    # 查詢該筆 username/newAccount 的數量
    sql = "SELECT COUNT(*) FROM member WHERE username = %s"
    val = (newAccount,)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    print(result)

    if (result[0] == 1):
        print("帳號已被註冊")
        return redirect("/error/?message=帳號已被註冊")
    elif (result[0] == 0):
        print("新的帳號")
        insertSql = "INSERT INTO member(name, username, password) VALUES(%s, %s, %s)"
        insertVal = (newName, newAccount, newPassword)
        cursor.execute(insertSql, insertVal)
        mydb.commit()
        print(cursor.rowcount, "新增資料成功")
        return redirect("/")

@app.route("/signin", methods=["POST"])
def signin():
    account = request.form["account"]
    password = request.form["password"]
    
    # 查詢該筆帳號的數量
    sql = "SELECT * FROM member WHERE username = %s AND password = %s"
    val = (account, password)
    cursor.execute(sql, val)
    result = cursor.fetchone()
    print(result)

    if result:
        # session["status"] = "已登入"
        session["name"] = result[1]
        return redirect("/member")
    elif account == "" or password == "":
        return redirect("/error/?message=請輸入帳號、密碼")
    else:
        return redirect("/error/?message=帳號、或密碼輸入錯誤")

@app.route("/member")
def member():
    if session["name"] == False:
        return redirect("/")
    name = session["name"]
    return render_template("member.html", name = str(name))

@app.route("/error/")
def error():
    msg = request.args.get("message","自訂的錯誤訊息")
    return render_template("error.html",errorMessages = str(msg))

@app.route("/signout")
def signout():
    session["name"] = False
    return redirect("/")

app.run(port=3000)

# 關閉游標
cursor.close()
# 關閉資料庫連線
mydb.close()