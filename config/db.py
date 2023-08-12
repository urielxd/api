from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://urielalemanelvira:muri1000@cluster0.nvuu9zm.mongodb.net/?retryWrites=true&w=majority"
conn = MongoClient(uri, server_api=ServerApi('1'))
