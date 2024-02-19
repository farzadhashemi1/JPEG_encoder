from PIL import Image


def convert_image_to_matrix(file_name):
    original_image = Image.open("./" + file_name)
    image_array = original_image.getdata()

    return image_array
