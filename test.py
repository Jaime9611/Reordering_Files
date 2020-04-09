import unittest
from pathlib import Path


class TestFileOrdering(unittest.TestCase):
    
    def test_files_sorted_exist(self):
        self.assertTrue(Path('./files_sorted').exists())

    def test_files_sorted_has_childs(self):

        state = True if list(Path('./files_sorted/').iterdir()) else False
        self.assertTrue(state)


if __name__ == '__main__':
    unittest.main()