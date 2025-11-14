import os


def write_file(working_directory, file_path, content):
    base = os.path.abspath(working_directory)
    target = os.path.abspath(os.path.join(base, file_path))
    if not target.startswith(base):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        if not os.path.exists(os.path.dirname(target)):
            os.makedirs(os.path.dirname(target))
        with open(target, "w") as f:
            f.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error writing file: {e}"

