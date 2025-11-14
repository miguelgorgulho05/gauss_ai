import os
from functools import reduce

def get_files_info(working_directory, directory="."):
    base = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(base, directory))
    if not full_path.startswith(base):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory\n' 
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory\n'
    
    try:
        contents = os.listdir(full_path)
    except PermissionError as e:
        return f"Error: {e}\n"

    listings = ""
    for item in contents:
        item_path = os.path.join(full_path, item)
        try:
            listing = f"- {item}: file_size={os.path.getsize(item_path)} bytes, is_dir={os.path.isdir(item_path)}"
            listings += listing + "\n"
        except PermissionError as e:
            return listings + f"Error: {e}\n"

    return f"Result for {"current" if directory == "." else f"'{directory}'"}' directory\n" + listings
