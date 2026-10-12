import unittest
from greet import greet, morning


class GreetTest(unittest.TestCase):
    def test_default_greet(self):
        self.assertEqual(greet(), "Hello, world!")

    def test_greet(self):
        self.assertEqual(greet("Ada"), "Hello, Ada!")

    def test_morning(self):
        self.assertEqual(morning("Ada"), "Good morning, Ada.")


if __name__ == "__main__":
    unittest.main()
