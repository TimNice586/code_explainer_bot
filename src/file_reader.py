import os

def read_python_files(folder_path):
    """
    Reads all .py files in the given folder.
    Returns a dictionary: {filename: code_content}.
    """
    code_files = {}
    for filename in os.listdir(folder_path):
        if filename.endswith(".py"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r") as f:
                code_files[filename] = f.read()
    return code_files


