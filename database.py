from os import environ
from dotenv import load_dotenv
from pymongo import MongoClient
from config import user, pwd, url, db 
# Connect to MongoDB Atlas
uri = f"mongodb+srv://{user}:{pwd}@{url}"
client = MongoClient(uri)
database = client.get_database(db)
users = database.get_collection("Users")

def create_user(fullname, email, password):
    """
    Creates a new user in the database.
    """
    if users.find_one({"email": email}):
        raise Exception("Email already in use!")

    doc = {
        "fullname": fullname,
        "email": email,
        "password": password,
    }
    user = users.insert_one(doc)
    return user


def fetch_user(data: dict):
    """
    Fetches a single user from the database.
    """
    user = users.find_one(data)
    return user



def update_user(email, data: dict):
    """
    Updates a single user in the database.
    """
    if users.find_one({"email": email}):
        users.update_one({"email": email}, {"$set": data})
        return "User updated!"
    else:
        raise Exception("User not found!")


def remove_user(data: dict):
    """
    Removes a single user from the database.
    """
    if users.find_one(data):
        users.delete_one(data)
        return "User removed!"
    else:
        raise Exception("User not found!")
    
def push_query(email: str ,data: dict):

    if users.find_one({"email": email}):
        users.update_one({"email": email}, {"$push": data})
        return "Query pushed!"
    else:
        raise Exception("User not found!")
