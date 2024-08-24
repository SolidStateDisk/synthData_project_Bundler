import os
import shutil
import json
import logging
from src.file_utils import transfer_files

def load_scripts_to_copy(config_file):
    """Load the list of scripts to be copied from a JSON configuration file."""
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)
        return config.get("scripts", [])
    except Exception as e:
        logging.error(f"Error loading scripts from config file: {e}")
        return []

def print_and_confirm_scripts(scripts_folder, script_files):
    """Print the list of scripts to copy, confirm they exist, and handle missing files."""
    missing_scripts = []
    found_scripts = []

    # Ensure the path points to the scripts subdirectory
    #scripts_folder = os.path.join(scripts_folder, 'scripts')

    print("The following scripts are to be copied:")

    for script in script_files:
        script_path = os.path.abspath(os.path.join(scripts_folder, script))
        print(f"Checking path: {script_path}")  # Debug: Print the absolute path being checked
        if os.path.exists(script_path):
            print(f" - {script} [FOUND]")
            found_scripts.append(script_path)
        else:
            missing_scripts.append(script)

    if missing_scripts:
        print("\nThe following scripts are missing and will not be copied:")
        for script in missing_scripts:
            print(f" - {script}")

    if found_scripts:
        print("\nThe following scripts will be copied:")
        for script in found_scripts:
            print(f" - {script}")

    if missing_scripts:
        logging.warning(f"The following scripts are missing: {', '.join(missing_scripts)}")

        # Ask the user if they want to proceed without the missing scripts
        confirm = input("Do you want to proceed with the remaining scripts? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Operation canceled.")
            logging.info("User canceled the operation due to missing scripts.")
            return False, found_scripts
    print ("-----------------------------------")
    for script in found_scripts:
        print (script)
    print ("-----------------------------------")


    return True, found_scripts

def copy_scripts(destination, scripts_folder, script_files):
    """Copy necessary scripts to the destination folder."""
    copied_scripts = []
    try:
        scripts_destination = os.path.join(destination, 'scripts')
        if not os.path.exists(scripts_destination):
            os.makedirs(scripts_destination)

        for script in script_files:
            script_path = os.path.join(scripts_folder, script)
            if os.path.exists(script_path):
                shutil.copy(script_path, scripts_destination)
                logging.info(f"Copied {script} to {scripts_destination}")
                copied_scripts.append(script)
            else:
                logging.warning(f"Script {script} not found in {scripts_folder}")
        
        print("\nThe following scripts were copied:")
        for script in copied_scripts:
            print(f" - {script}")
        
    except Exception as e:
        logging.error(f"Error copying scripts: {e}")
        print(f"Error copying scripts: {e}")

def handle_scripts(project_dir):
    """Handle the process of copying scripts."""
    scripts_config_file = 'config/scripts_to_copy.json'
    scripts_to_copy = load_scripts_to_copy(scripts_config_file)

    if not scripts_to_copy:
        print("No scripts found to copy.")
        logging.info("No scripts found to copy.")
        return False

    scripts_folder = os.path.join(os.getcwd(),"scripts") # Assuming scripts are in the current directory
    proceed, found_scripts = print_and_confirm_scripts(scripts_folder, scripts_to_copy)
    
    if not proceed:
        return False  # Exit if the user doesn't confirm

    #TODO: this line of code is not working bbecause we pass the file name and not the file path
    transfer_files(found_scripts, project_dir, '_scripts', 'copy')
    return True
