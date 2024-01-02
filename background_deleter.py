import requests
import os
from rembg import remove
from io import BytesIO
from PIL import Image


def process_image(output_folder, image_url):
    """Function to save and remove background from a user's picture"""

    # URL image getter
    response = requests.get(image_url)
    image_data = BytesIO(response.content)

    # Create object using PIL
    image = Image.open(image_data)

    # Save original file to same folder to avoid bugs
    temp_path = os.path.join(output_folder, 'downloaded_image.jpg')
    image.save(temp_path)

    # Using rembg to remove the background
    input_img = Image.open(temp_path)
    output_img = remove(input_img)

    # Saving result with proper file extension to output folder
    output_path = os.path.join(output_folder, 'output_image.png')
    output_img.save(output_path)
    print(f'Background removed, opening {output_folder}\n'
          f'──────────────────────────────────────────────────')

    # Clean up: remove temporary input image from disk
    os.remove(temp_path)

    # Automatically open output folder
    os.startfile(output_folder)


def main():
    print(f'┌─────── Welcome to background deleter! ─────────┐\n'
          f'|   Write STOP if you want to finish execution   |\n'
          f'└────────────────────────────────────────────────┘')

    # Creates new folder if it doesn't exist
    output_folder = 'output_images'

    # Function to process images
    while True:
        image_url = input('Enter the URL: ')

        # Check if folder exists
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        if image_url.lower() == 'stop':
            break
        else:
            try:
                process_image(output_folder, image_url)
            except Exception:
                print('An error has occurred, provide a valid URL!')


if __name__ == '__main__':
    main()
