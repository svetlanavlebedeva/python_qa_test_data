from files import JPEG_FILE_PATH

with open(JPEG_FILE_PATH, "rb") as file:
    img = file.read()
    with open('image.jpeg', "wb") as new_file:
        new_file.write(img)
