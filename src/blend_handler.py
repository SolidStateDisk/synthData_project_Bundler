import os
import shutil
import logging
from src.file_utils import transfer_files


def list_blend_files(directory):
    """List all .blend files in the given directory."""
    try:
        return [f for f in os.listdir(directory) if f.endswith('.blend')]
    except Exception as e:
        logging.error(f"Error listing .blend files: {e}")
        return []




def handle_blend_files(project_dir):
    """Handle the process of listing, selecting, and moving blend files."""
    current_directory = os.getcwd()
    blend_files = list_blend_files(current_directory)
    
    if not blend_files:
        print("No .blend files found.")
        logging.info("No .blend files found.")
        return
    
    print("Found the following .blend files:")
    for idx, file in enumerate(blend_files, start=1):
        print(f"{idx}. {file}")
    
    choices = input("Enter the numbers of the files to move, separated by spaces (or 'all'): ").split()

    if 'all' in choices:
        selected_files = blend_files
    else:
        selected_files = [blend_files[int(choice) - 1] for choice in choices if choice.isdigit()]

    transfer_files(selected_files, project_dir, 'blends', 'copy')
