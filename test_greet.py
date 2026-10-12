import unittest
from greet import goodnight, greet


class GreetTest(unittest.TestCase):
    def test_default_greet(self):
        self.assertEqual(greet(), "Hello, world!")

    def test_greet(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_goodnight(self):
        self.assertEqual(goodnight("Ada"), "Good night, Ada.")


if __name__ == "__main__":
    unittest.main()
