import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

def connect():
    uri = os.getenv("MONGO_URI"),

    client = MongoClient(uri, server_api=ServerApi('1'))

    return client[os.getenv("MONGO_CLUSTER")]