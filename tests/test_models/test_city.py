import unittest
from models.city import City
from models.base_model import BaseModel
from models.engine import storage_type

class TestCity(unittest.TestCase):
    """Test the City class"""

    def setUp(self):
        """Set up test environment"""
        self.city = City()

    def test_inheritance(self):
        """Test that City is a subclass of BaseModel"""
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """Test that City has the correct attributes"""
        if storage_type == 'db':
            self.assertTrue(hasattr(self.city, 'name'))
            self.assertTrue(hasattr(self.city, 'state_id'))
            self.assertEqual(self.city.name, '')
            self.assertEqual(self.city.state_id, '')
        else:
            self.assertTrue(hasattr(self.city, 'name'))
            self.assertTrue(hasattr(self.city, 'state_id'))
            self.assertEqual(self.city.name, '')
            self.assertEqual(self.city.state_id, '')

    def test_name_type(self):
        """Test that name is a string"""
        self.assertIsInstance(self.city.name, str)

    def test_state_id_type(self):
        """Test that state_id is a string"""
        self.assertIsInstance(self.city.state_id, str)

if __name__ == '__main__':
    unittest.main()