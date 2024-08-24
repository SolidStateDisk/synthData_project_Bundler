import os
import shutil
import logging
import random

def copy_img_folder(destination, img_folder):
    """Copy the 'img' folder to the destination with options to copy all or a random subset of images."""
    try:
        destination_img_folder = os.path.join(destination, 'img')
        if not os.path.exists(img_folder):
            logging.warning(f"img folder not found in {img_folder}")
            print(f"img folder not found in {img_folder}")
            return

        # List all files in the img folder
        images = [f for f in os.listdir(img_folder) if os.path.isfile(os.path.join(img_folder, f))]
        
        if not images:
            logging.info(f"The img folder at {img_folder} is empty.")
            print(f"The img folder at {img_folder} is empty.")
            return
        
        print(f"The img folder contains {len(images)} images.")
        logging.info(f"The img folder contains {len(images)} images.")

        choice = input("Do you want to copy all images or a random subset? (all/random): ").strip().lower()

        if choice == 'random':
            num_images = int(input(f"Enter the number of images to copy (1-{len(images)}): ").strip())
            if num_images < 1 or num_images > len(images):
                print("Invalid number of images. Operation canceled.")
                logging.warning(f"Invalid number of images entered: {num_images}. Operation canceled.")
                return
            images_to_copy = random.sample(images, num_images)
        else:
            images_to_copy = images  # Copy all images

        # Create destination img folder if it doesn't exist
        if not os.path.exists(destination_img_folder):
            os.makedirs(destination_img_folder)

        # Copy selected images
        for img in images_to_copy:
            shutil.copy(os.path.join(img_folder, img), destination_img_folder)
        
        print(f"Copied {len(images_to_copy)} images to {destination_img_folder}")
        logging.info(f"Copied {len(images_to_copy)} images to {destination_img_folder}")

    except Exception as e:
        logging.error(f"Error copying img folder: {e}")
        print(f"Error copying img folder: {e}")

def handle_img_folder(destination):
    """Main function to handle the process of copying the img folder."""
    current_directory = os.getcwd()
    img_folder = os.path.join(current_directory, 'img')
    copy_img_folder(destination, img_folder)
