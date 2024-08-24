from src.logger import setup_logging
from src.blend_handler import handle_blend_files
from src.script_handler import handle_scripts
from src.img_handler import handle_img_folder
from src.project_config import create_project_json
import os
def main():
    setup_logging()
    
    print("Starting the bundling process...")

    # Destination folder
    project_base_dir = 'projects'

    # Prompt the user for the destination folder name
    destination_folder = input("Enter the destination folder name: ")

    # Ensure the destination is within the /projects directory
    destination = os.path.join(project_base_dir, destination_folder)

    # Ensure the /projects directory exists
    if not os.path.exists(project_base_dir):
        os.makedirs(project_base_dir)

    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination):
        os.makedirs(destination)

    print(f"Files will be saved to: {destination}")
    # Handle scripts
    proceed = False
    print ("Handle scripts")
    proceed =handle_scripts(destination)
    if proceed == False:
        print ("EXIT")
        return

    # Handle blend files
    print ("handle blend files")
    handle_blend_files(destination)

    # Handle img folder
    print ("handle imgfolder")
    handle_img_folder(destination)

    # Create project JSON configuration
    project_name = input("Enter the project name: ")
    description = input("Enter the project description: ")
    create_project_json(project_name, description,destination)

if __name__ == "__main__":
    main()
