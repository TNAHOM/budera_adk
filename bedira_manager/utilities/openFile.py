import os
import inspect


def open_file(filename):
    """
    Reads the contents of a file located in the same directory as the caller's script.
    Args:
        filename (str): The filename to read (relative to the caller's script directory).
    Returns:
        str: The contents of the file.
    """
    # Get the caller's file path
    caller_frame = inspect.stack()[1]
    caller_file = caller_frame.filename
    caller_dir = os.path.dirname(os.path.abspath(caller_file))
    file_path = os.path.join(caller_dir, filename)
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()
