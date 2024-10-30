import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models import storage

#!/usr/bin/python
"""Unittest for Amenity class"""

class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Set up for the tests"""
        self.amenity = Amenity()

    def tearDown(self):
        """Tear down after tests"""
        del self.amenity

    def test_inheritance(self):
        """Test that Amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        """Test the attributes of Amenity"""
        self.assertTrue(hasattr(self.amenity, "name"))
        if storage_type == 'db':
            self.assertEqual(self.amenity.__tablename__, 'amenities')
            self.assertEqual(self.amenity.name, "")
        else:
            self.assertEqual(self.amenity.name, "")

    def test_to_dict(self):
        """Test to_dict method"""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')

    def test_str(self):
        """Test the __str__ method"""
        string = str(self.amenity)
        self.assertIn("[Amenity]", string)
        self.assertIn("id", string)
        self.assertIn("created_at", string)
        self.assertIn("updated_at", string)

    def test_save(self):
        """Test the save method"""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(self.amenity.updated_at, old_updated_at)

    def test_storage_type(self):
        """Test the storage type"""
        if storage_type == 'db':
            self.assertIsInstance(storage, DBStorage)
        else:
            self.assertIsInstance(storage, FileStorage)

if __name__ == "__main__":
    unittest.main()
