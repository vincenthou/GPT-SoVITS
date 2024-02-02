import os
import shutil

def create_folder_structure(output_folder, subfolders):
    """
    Create a specified folder structure.
    Parameters:
    - output_folder (str): The name of the main output folder.
    - subfolders (list of str): A list of subfolder names to be created within the main output folder.
    Returns:
    - dict: A dictionary indicating the status (True/False) of each folder creation.
    """
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # Create subfolders within the output folder
    folder_structure_status = {}
    for subfolder in subfolders:
        subfolder_path = os.path.join(output_folder, subfolder)
        folder_structure_status[subfolder] = False
        if not os.path.exists(subfolder_path):
            os.makedirs(subfolder_path)
            folder_structure_status[subfolder] = True
    return folder_structure_status

def delete_folder_structure(output_folder, subfolders):
    """
    Delete a specified folder structure.

    Parameters:
    - output_folder (str): The name of the main output folder.
    - subfolders (list of str): A list of subfolder names to be deleted within the main output folder.

    Returns:
    - dict: A dictionary indicating the deletion status (True/False) of each folder.
    """
    # Delete subfolders within the output folder
    folder_deletion_status = {}
    for subfolder in subfolders:
        subfolder_path = os.path.join(output_folder, subfolder)
        folder_deletion_status[subfolder] = False
        if os.path.exists(subfolder_path):
            shutil.rmtree(subfolder_path)
            folder_deletion_status[subfolder] = True

    # Delete the output folder if it's empty
    folder_deletion_status[output_folder] = False
    if os.path.exists(output_folder) and not os.listdir(output_folder):
        shutil.rmtree(output_folder)
        folder_deletion_status[output_folder] = True

    return folder_deletion_status
