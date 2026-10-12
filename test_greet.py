import unittest
from greet import farewell, greet


class GreetTest(unittest.TestCase):
    def test_default_greet(self):
        self.assertEqual(greet(), "Hello, world!")

    def test_greet(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_farewell(self):
        self.assertEqual(farewell("Ada"), "Goodbye, Ada!")

    def test_farewell_ignores_spaces(self):
        self.assertEqual(farewell("  Ada "), "Goodbye, Ada!")


if __name__ == "__main__":
    unittest.main()
