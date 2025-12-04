import unittest
from utils import arrs


class TestArrs(unittest.TestCase):

    def test_get_and_slice(self):
        self.assertEqual(arrs.get([1, 2, 3], 1, "test"), 2)
        self.assertEqual(arrs.get([], 0, "test"), "test")
        self.assertEqual(arrs.my_slice([]), [])
        self.assertEqual(arrs.my_slice([1, 2, 3]), [1, 2, 3])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 1, 10), [2, 3, 4, 5])
        self.assertEqual(arrs.my_slice([1, 2, 3, 4, 5], 1, 3), [2, 3])


if __name__ == '__main__':
    unittest.main()