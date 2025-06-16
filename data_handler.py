import json
from typing import List, Dict, Any

def load_data(file_path: str) -> List[Dict[str, Any]]:
    """
    Load book data from a JSON file.
    
    This function attempts to read and parse a JSON file containing book data.
    If the file doesn't exist or contains invalid JSON, it returns an empty list.
    
    Args:
        file_path: Path to the JSON file containing book data
        
    Returns:
        A list of book dictionaries. Returns an empty list if:
        - The file doesn't exist
        - The file contains invalid JSON
    """
    try:
        # Open the specified file in read mode
        with open(file_path, 'r') as f:
            # Parse the JSON content into a Python list of dictionaries
            return json.load(f)
    except FileNotFoundError:
        # Handle case where the file doesn't exist (common on first run)
        return []
    except json.JSONDecodeError:
        # Handle corrupted or invalid JSON data
        print("⚠️ Error: Corrupted data file. Starting with empty library.")
        return []

def save_data(file_path: str, data: List[Dict[str, Any]]) -> None:
    """
    Save book data to a JSON file.
    
    This function writes the current book collection to a JSON file
    with proper formatting. Handles potential write errors.
    
    Args:
        file_path: Path to the JSON file where data will be saved
        data: List of book dictionaries to be saved
    """
    try:
        # Open the specified file in write mode (creates or overwrites)
        with open(file_path, 'w') as f:
            # Serialize the data to JSON with 2-space indentation
            json.dump(data, f, indent=2)
    except IOError as e:
        # Handle file system errors (permissions, disk full, etc.)
        print(f"⚠️ Error saving data: {e}")
