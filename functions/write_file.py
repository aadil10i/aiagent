import os


def write_file(working_directory, file_path, content):
    abs_file_path = os.path.abspath(file_path)
    abs_working_dir = os.path.abspath(working_directory)

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        if not os.path.exists(file_path):
            os.makedirs(file_path)

    except OSError as e:
        print(f"Error: {e}")

    try:
        with open(file_path, "w") as f:
            f.write(content)
            print(
                f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
            )
    except OSError as e:
        return e
