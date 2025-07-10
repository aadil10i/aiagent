import os


def write_file(working_directory, file_path, content):
    if not file_path:
        return "Error: No file path provided."

    # First, join the working directory and file path to get the full target path.
    full_path = os.path.join(working_directory, file_path)

    # Then, get the absolute paths for comparison to prevent directory traversal attacks.
    abs_full_path = os.path.abspath(full_path)
    abs_working_dir = os.path.abspath(working_directory)

    if not abs_full_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    try:
        # Get the directory part of the path.
        directory = os.path.dirname(full_path)

        # Create the parent directory if it doesn't exist.
        if not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        # Now, write the file.
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)

        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except OSError as e:
        return f"Error: {e}"
