import os
import subprocess


def run_python_file(working_directory, file_path, *args):
    abs_working_dir = os.path.abspath(working_directory)
    abs_path_to_check = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_path_to_check.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_path_to_check):
        return f'Error: File "{file_path}" not found.'

    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        completed_process = subprocess.run(
            ["python", file_path, *args],
            cwd=working_directory,
            capture_output=True,
            text=True,
            timeout=30,
        )

        output_parts = []
        stdout = completed_process.stdout.strip()
        stderr = completed_process.stderr.strip()

        if stdout:
            output_parts.append(f"STDOUT: {stdout}")
        if stderr:
            output_parts.append(f"STDERR: {stderr}")

        if completed_process.returncode != 0:
            output_parts.append(f"Process exited with code {completed_process.returncode}")

        if not output_parts:
            return "No output produced."

        return "\n".join(output_parts)

    except subprocess.TimeoutExpired:
        return "Error: Timeout expired. The process took too long to complete."
    except Exception as e:
        return f"Error: executing Python file: {e}"
