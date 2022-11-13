import json

def add_ext(filename: str, extension: str='json') -> str:
    """Appends the file extension the given file name if needed.

    Args:
        filename (str): File name. With or without extension.
        extension (str): File extension. With or without dot. Defaults to JSON

    Returns:
        str: Full file name.
    """

    if not extension.startswith('.'):
        extension = f'.{extension}' 

    if not filename.endswith(extension):
        filename += extension

    return 'launchy/' + filename    


def read_json(filename: str):
    """Reads a JSON file and returns the loaded data.

    Args:
        name (str): The file to read (with or without .json)
    """

    with open(add_ext(filename), 'r') as f:
        return json.load(f)

def write_json(filename: str, data) -> None:
    """Writes data to a JSON file.

    Args:
        filename (str): The file to write to (with or without .json)
        data (_type_): The data to write to the file.
    """

    with open(add_ext(filename), 'w') as f:
        json.dump(data, f, indent=4, sort_keys=False)
