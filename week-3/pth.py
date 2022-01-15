# wehelp week-3
import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    # data=response.read().decode("utf-8") #取得網站原始碼+解碼
    data=json.load(response)
# print(data) 
import csv

#將景點名稱列表出來
allDetail=data["result"]["results"]
# print(allDetail)
# print(len(allDetail))

# with open("data.txt","w",encoding="utf-8") as file:  #寫入檔案至txt

with open('data.csv', 'w',encoding="utf-8", newline='') as csvfile:
    writer = csv.writer(csvfile)
    # fieldnames = ['stitle', 'area', 'longitude', 'latitude', 'picture1']
    # writer.writerow(['stitle', 'area', 'longitude', 'latitude', 'picture1'])
    for i in range(len(allDetail)):
        # print(i)
        # print("----------------")
        # print(allDetail[i]["stitle"])          #景點名稱
        # print(allDetail[i]["address"][0:3])   #區域
        # print(allDetail[i]["longitude"])      #經度
        # print(allDetail[i]["latitude"])       #緯度
        # print(allDetail[i]["file"]+"\n")      #所有圖檔網址

        jpg = ".jpg"
        firstFile = allDetail[i]["file"]
        firstPicture = firstFile[0:int(firstFile.lower().find(jpg))+4]
        # print(firstFile.lower().find(jpg))
        # print(firstFile[0:int(firstFile.lower().find(jpg))+4])
        # print(firstPicture)                     #第一張圖檔網址

        # 整理資料
        detail = allDetail[i]
        comma = ","
        str = [detail["stitle"],detail["address"][0:3],detail["longitude"],detail["latitude"],firstPicture]
        # print (comma.join(str))

        #寫入檔案至csv
        writer.writerow(str)           
             
# file.write(comma.join(str)+"\n")      #寫入檔案至txt
    

# print("-----  -----")