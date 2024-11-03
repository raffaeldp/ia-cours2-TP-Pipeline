from PIL import Image
import os
from datetime import datetime


def _expand2square(pil_img, background_color):
    width, height = pil_img.size
    if width == height:
        return pil_img
    elif width > height:
        result = Image.new("RGB", (width, width), background_color)
        result.paste(pil_img, (0, 0))
        return result
    else:
        result = Image.new("RGB", (height, height), background_color)
        result.paste(pil_img, (0, 0))
        return result


def clear_or_create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
    else:
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)


def check_and_create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


class ImageProcessor:
    """
    This class is used to process all the images present
    in the folder passed in the constructor

    Args:
        folder_path (string): The path to the folder that will be processed
    """

    _result_folder_path = "./datasets"

    def __init__(self, folder_path):
        self._folderPath = folder_path

    def process_folder(self, img_dimension):
        """
        This function take all the images contained in the
        folder passed in the constructor
        and resize them so they all have the same width and height.
        If the image can't be squared, colored padding is added.
        Then, all the images is saved in a new unique folder
        named after this format : %Y%m%d%H%M%S

        Args:
            img_dimension (int): The dimension that we
            want to apply to all our images
        """

        image_sources = os.listdir(self._folderPath)
        check_and_create_folder(self._result_folder_path)

        unique_folder_name = datetime.now().strftime("%Y%m%d%H%M%S")
        unique_folder = f"{self._result_folder_path}/{unique_folder_name}/"
        check_and_create_folder(unique_folder)

        for image_source in image_sources:
            self._process_image(
                image_source,
                img_dimension,
                f"{unique_folder}/{os.path.basename(image_source)}",
            )

    def _process_image(self, image_path, image_dimensions, image_dest):
        image = Image.open(f"{self._folderPath}/{image_path}")
        square_image = _expand2square(image, (114, 114, 114))
        square_image.resize((image_dimensions, image_dimensions))

        square_image.save(image_dest)
