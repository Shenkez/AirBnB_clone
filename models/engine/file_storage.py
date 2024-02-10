#!/usr/bin/python3
import json 

class FileStorage:
    __file_path = "file.json"
    __objects = {}


    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}". format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        json_obj = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(json_obj, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                loaded_objects = json.load(file)
                for key, value in loaded_objects.items():
                    class_name, obj_id = key.split(',')
                    obj_class = eval(class_name)
                    self.__objects[key] = obj_class(**value)
        except FileNotFoundError:
            pass
