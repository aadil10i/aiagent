import os


def get_file_content(working_directory, file_path):
    try:
        if not file_path:
            return "Error: No file path provided."

        path_to_check = os.path.join(working_directory, file_path)

        abs_working_dir = os.path.abspath(working_directory)
        abs_path_to_check = os.path.abspath(path_to_check)

        if not abs_path_to_check.startswith(abs_working_dir):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(path_to_check):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        MAX_CHARS = 10000
        MAX_PLUS_ONE = 10001

        with open(path_to_check, "r") as f:
            file_contents_string = f.read(MAX_PLUS_ONE)

            if len(file_contents_string) > MAX_CHARS:
                return (
                    file_contents_string[:MAX_CHARS]
                    + f'\n[File "{file_path}" trucated at {MAX_CHARS} characters]'
                )
            else:
                return file_contents_string
    except OSError as e:
        return f"Error: could not read file {file_path}: {e} "
