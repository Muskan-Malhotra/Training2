import sqlite3
conn = sqlite3.connect("accessment.db" )
cursor= conn.cursor()

cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
sql = """CREATE TABLE EMPLOYEE (
         EMPLOYEE_ID  INT primary key,
         EMPLOYEE_NAME  VARCHAR(25),
         MANAGER_ID INT,
         DATE_OF_HIRE DATE,
         JOBNAME VARCHAR(15),
         SALARY DECIMAL(10,2),
         DOB  DATE,
         ADDRESS VARCHAR(30),
         DEPARTMENT_ID INT  
         CONSTRAINT FK_DEPARTMENT  
         FOREIGN KEY(DEPARTMENT_ID)  
         REFERENCES DEPARTMENT(DEPARTMENT_ID)
         
         )"""
cursor.execute(sql)
print('Table is successfully created')
conn.close()

