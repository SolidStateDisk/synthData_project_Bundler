import os
import json
import logging
from datetime import datetime

def create_project_json(project_name, description,destination):
    """Create a project configuration JSON file in the /projects directory."""
    # Ensure the /projects directory exists
    projects_dir = os.path.join(os.getcwd(), 'projects')
    if not os.path.exists(destination):
        print ("project folder does not exists")
        #os.makedirs(projects_dir)

    # Create the project directory within /projects
    project_dir = os.path.join(projects_dir, project_name)
    #if not os.path.exists(project_dir):
     #   os.makedirs(project_dir)

    # Create the JSON configuration file
    project_info = {
        "project_name": project_name,
        "description": description,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "uploaded": False,
        "run": False
    }

    json_path = os.path.join(destination, 'project_config.json')
    try:
        with open(json_path, 'w') as json_file:
            json.dump(project_info, json_file, indent=4)
        logging.info(f"Created project JSON file at {json_path}")
        print(f"Created project JSON file at {json_path}")
    except Exception as e:
        logging.error(f"Error creating project JSON: {e}")
        print(f"Error creating project JSON: {e}")

    return project_dir  # Returning the project directory path for further use if needed
