"""Script to sort the files depending of a csv file data."""

import csv
from pathlib import Path


INPUT_DIR = './files' # Directory with the files
OUTPUT_DIR = './files_sorted' # Name of the new directory with the files sorted


def create_dir(files_dir):
    """Creates the OUPUT_DIR directory."""
    try:
        files_dir.mkdir()
    except FileExistsError:
        files = list(files_dir.iterdir())
        # Remove files if they exists
        if files:
            for f in files:
                f.unlink()


def move_files(input_dir, output_dir):
    """Move files from the INPUT_DIR to OUTPUT_DIR with the names in lowercase."""
    for f in input_dir.iterdir():
        new_file = output_dir / f'{f.stem.lower()}{f.suffix}'
        f.rename(new_file)


def main():
    """Main function of the script.

    Read the csv file and assigns a ID number to the corresponding file inside the files_sorted directory.
    """
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