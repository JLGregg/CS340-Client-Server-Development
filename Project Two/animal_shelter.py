from pymongo import MongoClient
from bson.objectid import ObjectId



class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, username, password): 
        #init to connect to mongodb without authentication
        #self.client = MongoClient('mongodb://localhost:48037')
        #init to connect to mongodb with authentication
        self.client = MongoClient('mongodb://%s:%s@localhost:48037/?authMechanism=DEFAULT&authSource=AAC'%(username, password))
        self.database = self.client['AAC']
    
    # Create an entry into the database
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
    
    # Read all of the database
    def read_all(self, data):
        cursor = self.database.animals.find(data, {'_id':False}) ## Return a pointer to a list of results
        return cursor
    
    # Read one entry of the database using the animal id
    def read(self, data):        
        result = self.database.animals.find_one(data) ## Returns only one document as a python directory
        return result
    
    # Update an entry in the database using the animal id and entering field to update
    def update(self, data, change):
        if data is not None:
            return self.database.animals.update(data,{"$set":change})
        else:
            print("Nothing to update because data parameter is empty")
       
    # Delete entry using animal ID
    def delete(self, data):
        if data is not None:
            return self.database.animals.delete_one(data)
        else:
            print("Nothing to delete, data parameter is empty")
        
        
        