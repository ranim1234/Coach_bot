import certifi
from pymongo import MongoClient



client = MongoClient("mongodb+srv://yosra:yosra123@cluster0.oozum.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=certifi.where())

db = client.produit
db1 = client.entrepise


collection_name = db["produit"]
collection_name1 = db1["entreprise"]

