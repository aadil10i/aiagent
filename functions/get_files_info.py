import os
from google.genai import types


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
        try:
            full_path = os.path.join(path_to_check, file_name)
            file_size = os.path.getsize(full_path)
            is_dir = os.path.isdir(full_path)

            print(f"- {file_name}: file_size={file_size} bytes, is_dir={is_dir}")

        except OSError as e:
            print(f"Error: could not process file name {e}")


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)


if __name__ == "__main__":
    script_dir = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(script_dir, ".."))

    get_files_info(project_root)
