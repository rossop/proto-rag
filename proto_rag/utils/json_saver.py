import json
from typing import Any

def save_to_json(data: Any, output_path: str) -> None:
    """Saves data to a JSON file.

    Args:
        data (Any): The data to save.
        output_path (str): The path to the output JSON file.
    """
    with open(output_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)