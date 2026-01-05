import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from string_distance_metrics.distances.levenshtein import levenshtein_distance

class TestLevenshtein(unittest.TestCase):
    def test_identical(self):
        self.assertEqual(levenshtein_distance("hola", "hola"), 0)

    def test_simple_edit(self):
        self.assertEqual(levenshtein_distance("gato", "pato"), 1)

    def test_empty(self):
        self.assertEqual(levenshtein_distance("", "abc"), 3)

if __name__ == '__main__':
    unittest.main()