import argparse
from pathlib import Path
from typing import List


def pick_dir(file_name: str, path: str) -> str:
    """
    Splits the file name to determine its directory
    :param path: the folder path required for files
    :param file_name: the required file to save
    :return: the directory name
    """
    directory = file_name.split('-')[0]
    return f'{path}/{directory}'


def batch_files(file_list: List[Path], path: str) -> None:
    """
    Moves files in a batch to their corresponding subdirectories
    :param file_list: list of files to move
    :param path: path to directory containing files
    """
    for file in file_list:

        # just looking for file, skip the directory
        if file.is_dir():
            continue

        # extracting the file and figuring out where to locate it
        file_name = file.name
        directory = pick_dir(file_name, path)

        directory_path = Path(directory)

        # make new directory if the category's directory not found.
        if not directory_path.is_dir():
            directory_path.mkdir()

        # reassigning the file into its correct path
        file.rename(directory_path.joinpath(file_name))


def main(path: str, batch_size: int = 100) -> None:
    """
    Organizes files in a directory by moving them to corresponding subdirectories
    :param path: path to directory containing files
    :param batch_size: size of file batch to process
    """
    file_list = list(Path(path).iterdir())

    # process files in batches
    for i in range(0, len(file_list), batch_size):
        batch_files(file_list[i:i + batch_size], path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Organize files in a directory by moving them to corresponding subdirectories')
    parser.add_argument('--path', metavar='path', type=str, help='path to directory containing files')
    parser.add_argument('--batch-size', dest='batch_size', type=int, help='size of file batch to process')

    args = parser.parse_args()

    main(args.path, args.batch_size)
