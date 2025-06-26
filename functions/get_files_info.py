import os
from collections import defaultdict


def get_files_info(working_directory, directory=None):
    if directory is None:
        path_to_check = working_directory
    else:
        path_to_check = os.path.join(working_directory, directory)

    abs_working_dir = os.path.abspath(working_directory)
    abs_path_to_check = os.path.abspath(path_to_check)

    if not abs_path_to_check.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(path_to_check):
        return f'Error: "{directory}" is not a directory'

    file_contents = os.listdir(path_to_check)

    for file_name in file_contents:
        full_path = os.path.join(path_to_check, file_name)
        file_size = os.path.getsize(full_path)
        is_dir = os.path.isdir(full_path)

        print(f"- {file_name}: file_size={file_size} bytes, is_dir={is_dir}")


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(script_dir, ".."))

    get_files_info(project_root)


# os.listdir(): List the contents of a directory
# os.path.getsize(): Get the size of a file
# os.path.isfile(): Check if a path is a file
# .join(): Join a list of strings together with a separator
