import os


def get_files_info(working_directory, directory="."):
    base = os.path.abspath(working_directory)
    target = os.path.abspath(os.path.join(base, directory))
    if not target.startswith(base):
        return f"Error: Cannot list {directory} as it is outside the permitted working directory"
    if not os.path.isdir(target):
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        for file in os.listdir(target):
            file_path = os.path.join(target, file)
            file_size = os.path.getsize(file_path)
            is_dir = os.path.isdir(file_path)
            files_info.append(
                f"- {file}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"
