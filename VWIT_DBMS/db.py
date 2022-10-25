'''
import sqlite3
try:
  #open database cooncetion
  conn=sqlite3.connect("School.db")
#prepare a cursor object using cursor() method
  cursor = conn.cursor()

  print("connected")
except:
  print("Server not found")

conn.close()
'''
    

import sqlite3
conn = sqlite3.connect("School.db" )

cursor = conn.cursor()
# cursor.execute("DROP TABLE IF EXISTS Teacher_Detail")
# sql = """CREATE TABLE Teacher_Detail (
#          ID INT,
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          SEX CHAR(1),
#          SUBJECT CHAR(20),
#          INCOME FLOAT )"""
# cursor.execute(sql)
# print('Table is successfully created')
# conn.close()


sql1= 'INSERT INTO Teacher_Detail(ID,FIRST_NAME,LAST_NAME, SEX,SUBJECT, INCOME)VALUES(103,"John", "Thomas", "M","Math", 20000)'
sql2= 'INSERT INTO Teacher_Detail(ID,FIRST_NAME,LAST_NAME, SEX,SUBJECT, INCOME)VALUES(104,"Sam", "Johnson", "M","Science", 40000)'
sql3= 'INSERT INTO Teacher_Detail(ID,FIRST_NAME,LAST_NAME, SEX,SUBJECT, INCOME)VALUES(1011,"Martina", "Lee", "F","English", 45000)'
try:
   cursor.execute(sql1)
   cursor.execute(sql2)
   cursor.execute(sql3)
   print('Data successfully inserted')
   conn.commit()
except:
   conn.rollback()
   print('Data not inserted')




