import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage


if storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()