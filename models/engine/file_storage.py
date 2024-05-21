#!/usr/bin/python3
import json 
import models
from os.path import exists
"""file storage for airbnb clone"""

class FileStorage:
    """file storage class"""

    __file_path = "file.json"
    __objects = {}


    def all(self):
        """return the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """set object{} to obj"""
        key = "{}.{}". format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serialization to json"""
        json_obj = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(json_obj, file)

    def reload(self):
        """deserializes the JSON file to __objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        if exists(self.__file_path):
            with open(self.__file_path) as file:
                decereal = json.load(file)
            for keys in decereal.keys():
                if decereal[keys]['__class__'] == "BaseModel":
                    self.__objects[keys] = BaseModel(**decereal[keys])
                elif decereal[keys]['__class__'] == "User":
                    self.__objects[keys] = User(**decereal[keys])
                elif decereal[keys]['__class__'] == "State":
                    self.__objects[keys] = State(**decereal[keys])
                elif decereal[keys]['__class__'] == "City":
                    self.__objects[keys] = City(**decereal[keys])
                elif decereal[keys]['__class__'] == "Amenity":
                    self.__objects[keys] = Amenity(**decereal[keys])
                elif decereal[keys]['__class__'] == "Place":
                    self.__objects[keys] = Place(**decereal[keys])
                elif decereal[keys]['__class__'] == "Review":
                    self.__objects[keys] = Review(**decereal[keys])
