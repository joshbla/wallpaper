from PIL import Image
import os

i = 1

folder_path = os.getcwd()
for file_name in os.listdir(folder_path):
    if file_name.endswith('.png'):
        file_path = os.path.join(folder_path, file_name)
        # Open the image file
        with Image.open(file_path) as img:
            # Resize the image to 300x300
            img = img.resize((300, 300))
            # Save the resized image with a new file name
            new_file_name = "example logo " + str(i) + ".png"
            new_file_path = os.path.join(folder_path, new_file_name)
            img.save(new_file_path)
        i += 1