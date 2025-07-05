#file type checker after uploaded file
def filetype_checker(file_path: str)-> str:
    """
    Checks if the file type of the given file path is valid.

    Args:
        file_path (str): The path to the file to check.

    Returns:
        str: "valid" if the file type is valid, "invalid" otherwise.

    Notes:
        This function checks if the file path ends with one of the accepted file types.
    """
    accepted_types = ["png", "jpg", "jpeg", "webp"]
    # Check if the file path ends with one of the accepted file types
    file_ext = file_path.endswith(tuple(accepted_types))

    if file_ext:
        return "valid"
    
    return "invalid"






