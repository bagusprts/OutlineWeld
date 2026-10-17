# test_outlineweld.py
"""
Tests for OutlineWeld module.
"""

import unittest
from outlineweld import OutlineWeld

class TestOutlineWeld(unittest.TestCase):
    """Test cases for OutlineWeld class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OutlineWeld()
        self.assertIsInstance(instance, OutlineWeld)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OutlineWeld()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
