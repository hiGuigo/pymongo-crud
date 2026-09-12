from pymongo import MongoClient
from pymongo.server_api import ServerApi

def connect():
    uri = "string connection"

    client = MongoClient(uri, server_api=ServerApi('1'))

    return client["nome da sua collection"]