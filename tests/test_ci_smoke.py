import unittest


class TestCISmoke(unittest.TestCase):
    def test_basic_arithmetic(self):
        self.assertEqual(2 + 2, 4)
