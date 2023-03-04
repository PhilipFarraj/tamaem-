# File Organizer

This Python script moves files from a specified directory to subdirectories based on the first part of their names. For example, a file named "example-image.jpg" would be moved to a subdirectory called "example".

## Requirements

- Python 3.x
- `pathlib` module (included in the Python standard library)

## Usage

1. Clone or download the repository.
2. Open a terminal or command prompt and navigate to the directory where the `file_organizer.py` script is located.
3. Run the script with the following command, replacing `folder_name` with the name of the directory containing the files you want to organize with the batch size (number of files needed):
**_python3 file_organizer.py --path 'filename' --batch-size 'batch-size'_**

For example, if you want to organize files in a directory called "files", run the following command:

**_python3 file_organizer.py --path files --batch-size 100_**


4. The script will move the files to subdirectories based on the first part of their names. For example, a file named "example-image.jpg" would be moved to a subdirectory called "example". If a subdirectory for a file's category doesn't exist, the script will create one.


## Acknowledgments

This script was created as a task to be handed in and may not be suitable for all use cases. Use at your own risk.

Please let me know if you have any questions or issues with the script.


