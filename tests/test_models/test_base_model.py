import unittest
from datetime import datetime
from models.base_model import BaseModel
import uuid

#!/usr/bin/python3
"""Defines unittests for models/base_model.py."""


class TestBaseModel(unittest.TestCase):
    """Unittests for testing the BaseModel class."""

    def setUp(self):
        """Set up test methods."""
        self.model = BaseModel()

    def test_instantiation(self):
        """Test that a BaseModel instance is correctly instantiated."""
        self.assertIsInstance(self.model, BaseModel)
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_unique_id(self):
        """Test that each BaseModel instance has a unique id."""
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_str(self):
        """Test the __str__ method of BaseModel."""
        string = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), string)

    def test_save(self):
        """Test the save method of BaseModel."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test the to_dict method of BaseModel."""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

    def test_delete(self):
        """Test the delete method of BaseModel."""
        self.model.delete()
        # Assuming storage.delete() removes the instance from storage
        # This test would need to be expanded based on the storage implementation

if __name__ == "__main__":
    unittest.main()