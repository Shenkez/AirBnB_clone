#!/usr/bin/python3

import uuid
from datetime import datetime
import models
#from models import storage
''' this defines the base class'''


class BaseModel:

    def __init__(self, *args, **kwargs):
        if kwargs: #if kwargs not empty
            #kwargs.pop('__class__', None) #remove __class__key frm d dict
            #iterate through the kwargs
            for key, value in kwargs.items():
                if key != '__class__':
                    #if the current kwargs is either of 2 in the list above
                    if key in ['created_at', 'updated_at']:
                        #convert frm str reps to datetime reps
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        #setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    setattr(self, key, value)
                    
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.:storage.save()

    def to_dict(self):
        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = type(self).__name__
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()

        return dict_obj
