# create user record 
# get latest user schema
# update user record 

import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class DatabaseManger:
    def __init__(self, db_name: str, collection_name: str):
        self.client = None
        self.db_name = db_name
        self.collection_name = collection_name
        self.connect()

    def connect(self):
        try:
            self.client = MongoClient(os.getenv("MONGO_URI", "mongodb+srv://chajaykrishna5:G6g1iDGbPVo7X5BG@cluster0.irgo9zq.mongodb.net/"))
            print("Database connection established.")
        except ConnectionFailure as e:
            print(f"Failed to connect to the database: {e}")

    def get_collection(self):
        if self.client:
            return self.client[self.db_name][self.collection_name]
        else:
            raise ConnectionError("No database connection established.")

    def close_connection(self):
        if self.client:
            self.client.close()
            print("Database connection closed.")
        
    def get_user_information(self, user_id: str):
        """
        Retrieves user information from the database.
        
        Args:
            user_id (str): The ID of the user to retrieve information for.
        
        Returns:
            dict: User information if found, otherwise None.
        """
        print("All available databases: ", self.client.list_database_names())
        print("Available collections in database:", self.client[self.db_name].list_collection_names())
        collection = self.get_collection()
        user_info = collection.find_one({"_id": user_id})
        return user_info
    
    def create_user_record(self, user_info: dict):
        """
        Creates a new user record in the database.
        
        Args:
            user_info (dict): A dictionary containing user information.
        
        Returns:
            str: The ID of the created user record.
        """
        collection = self.get_collection()
        result = collection.insert_one(user_info)
        return str(result.inserted_id)