#!/usr/bin/python3
"""
This module instantiates an object of storage depending on type
Contains the model of all objects
"""
from os import getenv


if getenv('HBNB_TYPE_STORAGE') == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    # Using file storage
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
