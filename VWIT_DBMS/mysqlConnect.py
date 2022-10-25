import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="root123"
)

print(dataBase)
cursorObj = dataBase.cursor()
cursorObj.execute("create database Hithere")
dataBase.close()
# //pip install mysql-connector-python
#
