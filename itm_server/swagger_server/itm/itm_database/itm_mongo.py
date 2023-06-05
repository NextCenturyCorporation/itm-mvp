from pymongo import MongoClient
from urllib.parse import quote_plus
import json
import os
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    '''Custom JSON encoder that encodes MongoDB ObjectId instances as strings.'''
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


class MongoDB:
    def __init__(self, username, password, host, port, database):
        username = quote_plus(username)
        password = quote_plus(password)
        self.client = MongoClient(f'mongodb://{username}:{password}@{host}:{port}/')
        self.db = self.client[database]

    def insert_data(self, collection, data):
        result = self.db[collection].insert_one(data)
        return result.inserted_id

    def retrieve_data(self, collection, object_id):
        retrieved_data = self.db[collection].find_one({"_id": object_id})
        # Instead of encoding to JSON string here, just return the Python dict
        return retrieved_data

    def write_to_json_file(self, data):
        # Convert the ObjectId back to string if necessary
        if isinstance(data, dict):
            for k, v in data.items():
                if isinstance(v, ObjectId):
                    data[k] = str(v)

        filepath = 'itm_mvp_local_output/'

        # Make directory if it doesn't exist
        os.makedirs(filepath, exist_ok=True)

        # Get the list of all json files in directory
        file_list = [f for f in os.listdir(filepath) if os.path.isfile(os.path.join(filepath, f)) and f.endswith('.json')]

        # Calculate file_number based on the number of files
        file_number = len(file_list) + 1
        file_name = f'itm_mvp_output_{file_number}.json'
        full_filepath = filepath + file_name

        with open(full_filepath, 'w') as f:
            # Convert Python dictionary to JSON and write to file
            json.dump(data, f, indent=4)
