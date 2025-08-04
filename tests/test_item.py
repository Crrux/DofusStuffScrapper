import unittest
from item import Equipement

class TestItem(unittest.TestCase):
    def setUp(self):
        self.equipement = Equipement("Epée")

     # Test cases for the Equipement class
    def test_initialization(self):
        self.assertEqual(self.equipement.name, "Epée")
        self.assertEqual(self.equipement.compos, [])
        self.assertIsInstance(self.equipement.name, str)
        self.assertIsInstance(self.equipement.compos, list)

    # test cases for the add_compos method
    def test_add_component(self):
        self.equipement.add_compos(("Fer", 50))
        self.assertEqual(self.equipement.compos, [("Fer", 50)])
        self.equipement.add_compos(("bois", '10'))
        self.assertEqual(self.equipement.compos, [("Fer", 50), ("bois", 10)])



if __name__ == '__main__':
    unittest.main()