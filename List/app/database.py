from pymongo import MongoClient

client_host = "localhost"
client_port = 27017

client = MongoClient(client_host, client_port)
database = client["database"]