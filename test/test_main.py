
import unittest
from main import add


class TestMathOperation(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)
