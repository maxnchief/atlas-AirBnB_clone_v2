import unittest
from models.city import City
from models.base_model import BaseModel
from sqlalchemy.orm import relationship

class TestCity(unittest.TestCase):
    """Test the City class"""

    def setUp(self):
        """Set up test environment"""
        self.city = City()

    def test_inheritance(self):
        """Test that City inherits from BaseModel"""
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """Test City attributes"""
        self.assertTrue(hasattr(self.city, "name"))
        self.assertTrue(hasattr(self.city, "state_id"))
        if hasattr(self.city, "places"):
            self.assertIsInstance(self.city.places.property, relationship)

    def test_name_type(self):
        """Test that name is a string"""
        self.assertIsInstance(self.city.name, str)

    def test_state_id_type(self):
        """Test that state_id is a string"""
        self.assertIsInstance(self.city.state_id, str)

if __name__ == "__main__":
    unittest.main()