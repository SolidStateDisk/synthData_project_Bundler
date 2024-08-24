import os
import shutil
import logging

def transfer_files(files, destination, subfolder, copy_or_move):
    """Transfer selected files to the specified subfolder within the destination directory, either by copying or moving them."""
    try:
        # Create the destination subfolder inside the destination directory
        final_destination = os.path.join(destination, subfolder)
        if not os.path.exists(final_destination):
            os.makedirs(final_destination)
        
        # Transfer each file to the destination subfolder
        for file in files:
            if copy_or_move == 'move':
                shutil.move(file, os.path.join(final_destination, os.path.basename(file)))
                action = "Moved"
            elif copy_or_move == 'copy':
                shutil.copy(file, os.path.join(final_destination, os.path.basename(file)))
                action = "Copied"
            else:
                logging.error(f"Invalid operation: {copy_or_move}")
                print(f"Invalid operation: {copy_or_move}")
                return
        
        logging.info(f"{action} {len(files)} files to {final_destination}")
        print(f"{action} {len(files)} files to {final_destination}")
    except Exception as e:
        logging.error(f"Error transferring files: {e}")
        print(f"Error transferring files: {e}")
