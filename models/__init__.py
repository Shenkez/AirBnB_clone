#!/usr/bin/python3
'''__init__ method: This code is meant to initialize the FileStorage
class from the models.engine.file_storage module and reload data from a JSON file'''

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()

