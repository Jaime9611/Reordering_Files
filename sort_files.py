"""Script to sort the files depending of a csv file data."""

import csv
import logging
from pathlib import Path

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

INPUT_DIR = './files'
OUTPUT_DIR = './files_sorted'


def create_dir(files_dir):
    try:
        files_dir.mkdir()
    except FileExistsError:
        files = list(files_dir.iterdir())
        if files:
            for f in files:
                f.unlink()
        
        files_dir.rmdir()
        files_dir.mkdir()


def move_files(input_dir, output_dir):
    for f in input_dir.iterdir():
        new_file = output_dir / f'{f.stem.lower()}{f.suffix}'
        logging.debug(new_file)
        f.rename(new_file)


def main():
    with open('data/data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        input_dir = Path(INPUT_DIR)
        output_dir = Path(OUTPUT_DIR)
        create_dir(output_dir)
        move_files(input_dir, output_dir)

        for index, row in enumerate(reader, 1):
            product_name = row['PRODUCT'].lower()
            for f in output_dir.iterdir():
                if f.stem == product_name:
                    target = Path(output_dir / f'{index}_{product_name}{f.suffix}')
                    f.rename(target)




if __name__ == "__main__":
    main()