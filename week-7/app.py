from flask import Flask, request, redirect, render_template, session 
from flask import jsonify
import json
from flask import Response
import mysql.connector

app = Flask(__name__,) 
app.secret_key="celesteSecret" # 設定 Session 密鑰：可以填寫任何字串但不告訴別人
app.config["JSON_AS_ASCII"] = False # 解決中文亂碼

# 連接 MySQL/MariaDB 資料庫
mydb = mysql.connector.connect(
    host = "127.0.0.1",      # 主機名稱
    database="website",      # 資料庫名稱
    user = "root",           # 帳號
    password = "0117"        # 密碼
)
print(mydb)
cursor = mydb.cursor()


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


@app.route("/api/members")
def apiMembers():
    # sql = "SELECT * FROM member WHERE username = 'test2' "
    # cursor.execute(sql)
    username = request.args.get("username","錯誤資料")
    sql = "SELECT * FROM member WHERE username = %s "
    val = (username,)  #逗號很重要
    cursor.execute(sql, val)    

    result = cursor.fetchone()  
    print(result)  # (2, 'Celeste', 'test1', 'test1', 500, datetime.datetime(2022, 1, 30, 14, 11, 1))
    if(result):
        data = {
            "id" : result[0],
            "name" : result[1],
            "username" : result[2]
        }
        print(data)  # {'id': 2, 'name': 'Celeste', 'username': 'test1'}
    else:
        data = None
    return jsonify({"data":data}) 

    # try:
    #     sql = "SELECT * FROM member WHERE username = 'test2' "
    #     cursor.execute(sql)
    #     # username = request.args.get("username","錯誤")
    #     # sql = "SELECT * FROM member WHERE username = %s "
    #     # val = (username)
    #     # cursor.execute(sql, val)    
    #     result = cursor.fetchone()  
    #     print(result)  # (2, 'Celeste', 'test1', 'test1', 500, datetime.datetime(2022, 1, 30, 14, 11, 1))
    #     data = {
    #         "id" : result[0],
    #         "name" : result[1],
    #         "username" : result[2]
    #     }
    #     print(data)  # {'id': 2, 'name': 'Celeste', 'username': 'test1'}
    #     return jsonify({"data":data})
    # except:
    #     return jsonify({"data":None}) 





app.run(port=3000)

# 關閉游標
cursor.close()
# 關閉資料庫連線
mydb.close()