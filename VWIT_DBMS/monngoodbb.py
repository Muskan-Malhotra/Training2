# import mongo client to connect
from pymongo import MongoClient
# Creating instance of mongoclient  
client = MongoClient()
# Creating database  
db = client.testdb 
employee = {"id": "1010",  "name": "John",  "profession": "Software Developer"}
# Creating collection
employees = db.employees
# Inserting data  
employees.insert_one(employee)
# Fetching data
data=employees.find_one()
print('Fetched data:',data)
