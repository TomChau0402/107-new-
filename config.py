import pymongo
import certifi

connection_string = "mongodb+srv://test:FSDIflask@cluster0.glkph.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = pymongo.MongoClient(connection_string, tlsCAFile=certifi.where())
db  = client.get_database("ch54-tom")