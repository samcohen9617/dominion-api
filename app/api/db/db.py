from pymongo import MongoClient


def connect_db(app):
    """
    Connects app to required databases
    """
    return MongoClient("mongodb://localhost:27017").get_database("DOMINION_EXTENSION")
