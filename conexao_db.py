from pymongo import MongoClient

host= 'localhost'
port= 27017
username = "admin"
password= "admin"
database = "petshop"

client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/")
db = client[database]



