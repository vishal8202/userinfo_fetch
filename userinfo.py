import requests
import sys
import mysql.connector
import json

try:
    mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'userinfofetch_db')
except mysql.connector.Error as e:
    sys.exit(e)

mycursor = mydb.cursor()

data = requests.get("https://reqres.in/api/users?page=1").text

data_info = json.loads(data)

for i in data_info["data"]:
    sql = "INSERT INTO `userinfofetch`(`email`, `first_name`, `last_name`, `avathar`) VALUES ('"+i['email']+"','"+i['first_name']+"','"+i['last_name']+"','"+i['avatar']+"')"
    #data = (i['email'],i['first_name'],) 
    mycursor.execute(sql)
    mydb.commit()
    print('Inserted successfully !!!',i['id'])