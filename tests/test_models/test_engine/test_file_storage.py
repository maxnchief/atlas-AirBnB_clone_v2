import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os
import json

class TestFileStorage(unittest.TestCase):
    """Test the FileStorage class"""

    def setUp(self):
        """Set up for the tests"""
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.storage.new(self.obj)
        self.file_path = FileStorage._FileStorage__file_path

    def tearDown(self):
        """Tear down after tests"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
        FileStorage._FileStorage__objects = {}

    def test_new(self):
        """Test that new adds an object to the storage"""
        self.assertIn(f'BaseModel.{self.obj.id}', self.storage.all())

    def test_save(self):
        """Test that save properly saves objects to file"""
        self.storage.save()
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        self.assertIn(f'BaseModel.{self.obj.id}', data)

    def test_reload(self):
        """Test that reload properly loads objects from file"""
        self.storage.save()
        self.storage.reload()
        self.assertIn(f'BaseModel.{self.obj.id}', self.storage.all())

    def test_delete(self):
        """Test that delete removes an object from storage"""
        self.storage.delete(self.obj)
        self.assertNotIn(f'BaseModel.{self.obj.id}', self.storage.all())

    def test_all(self):
        """Test that all returns the storage dictionary"""
        self.assertEqual(self.storage.all(), FileStorage._FileStorage__objects)

    def test_all_with_class(self):
        """Test that all returns only objects of a specific class"""
        self.assertEqual(self.storage.all(BaseModel), {f'BaseModel.{self.obj.id}': self.obj})

if __name__ == '__main__':
    unittest.main()