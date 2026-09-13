import unittest

from intervals import inclusive_total


class InclusiveTotalTests(unittest.TestCase):
    def test_positive_interval(self):
        self.assertEqual(inclusive_total(1, 3), 6)

    def test_single_endpoint(self):
        self.assertEqual(inclusive_total(4, 4), 4)

    def test_crosses_zero(self):
        self.assertEqual(inclusive_total(-2, 2), 0)

    def test_rejects_reversed_bounds(self):
        with self.assertRaises(ValueError):
            inclusive_total(3, 1)


if __name__ == "__main__":
    unittest.main()
