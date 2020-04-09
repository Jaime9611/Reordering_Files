"""Script to sort the files depending of a csv file data."""

import csv
import logging
from pathlib import Path

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

LOCATION = './files_sorted'

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



def main():
    with open('data/data.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        files_dir = Path(LOCATION)
        create_dir(files_dir)

        for row in reader:
            file_name = row['PRODUCT'].lower()
            logging.info(file_name)


if __name__ == "__main__":
    main()