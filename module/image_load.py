# load image from json file
import json
import os

"""module provides functions for collecting images information from JSON files and extracting image infor for process."""

def load_image_from_json(file_path: str) -> dict:
    """
    Loads image data from a JSON file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Image data loaded from the JSON file.
    """
    with open(file_path, "r") as jsonFile:
        data = json.load(jsonFile)
    return data


def extract_image_path(image_dict: dict):
    """
    Extracts image paths from the loaded image data.

    Args:
        image_dict (dict): Image data loaded from the JSON file.

    Returns:
        tuple: A tuple containing a list of image paths and a list of image IDs.
    """
    path_database = []
    id_list = []
    for key, dict_item in image_dict.items():
        for item in dict_item:
            path_database.append(item["image_path"])
            id_list.append(item["id"])

    return path_database, id_list  

def get_image_path(base_dir: str):
    """
    Retrieves a list of image paths from a given base directory.

    Args:
        base_dir (str): The base directory to search for images.

    Returns:
        list: A list of image paths found in the base directory.

    Notes:
        This function uses the `os` module to walk the directory tree and find image files.
        It returns a list of image paths, where each path is a string representing the full path to an image file.
    """
    directory = os.walk(base_dir)
    
    # Initialize an empty list to store image paths
    image_list = []
    count = 0
    # Walk the directory tree starting from the base directory
    for path, subdirs, files in directory:
        # Iterate over each file in the current directory
        for file in files:
            count += 1
            # Construct the full path to the file
            temp = base_dir + "/" + file
            # Add the image path to list
            image_list.append([count,temp])
        
    return image_list

# testing function
# print(get_image_path("static/image/gallery"))
