import unittest
from pathlib import Path

import sort_files

file_names = [
    'CAr.txt',
    'cEllPhone.txt',
    'Laptop.txt',
    'pants.txt',
    'coLLars.txt',
    'pen.txt',
    'ShoeS.txt',
    'Socks.txt',
    'tv.txt',
    'WaTch.txt',
]


class TestFileOrdering(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        Path('files').mkdir()
        for f in file_names:
            Path('files/', f).touch()

        sort_files.main()

    def test_files_sorted_exist(self):
        self.assertTrue(Path('./files_sorted').exists())

    def test_files_sorted_has_childs(self):
        state = True if list(Path('./files_sorted/').iterdir()) else False
        self.assertTrue(state)

    def test_correct_file_names(self):
        files = [
            '10_pen.txt',
            '1_tv.txt',
            '2_cellphone.txt',
            '3_car.txt',
            '4_watch.txt',
            '5_laptop.txt',
            '6_pants.txt',
            '7_shoes.txt',
            '8_collars.txt',
            '9_socks.txt'
        ]

        actual_files =[f.name for f in Path('./files_sorted').iterdir()]
        self.assertEqual(files, actual_files)


if __name__ == '__main__':
    unittest.main()