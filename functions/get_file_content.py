import os
from config import *


def get_file_content(working_directory, file_path):
    base = os.path.abspath(working_directory)
    target = os.path.abspath(os.path.join(base, file_path))
    if not target.startswith(base):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(target, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        if len(file_content_string) == MAX_CHARS:
            file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]' 
        return file_content_string
    except Exception as e:
        return f"Error reading file: {e}"
