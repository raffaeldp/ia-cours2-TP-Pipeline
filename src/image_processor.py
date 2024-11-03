from PIL import Image
from datetime import datetime
import os

from src.folder_utils import ensure_folder_exists


def _expand_image_to_square(
    image: Image, background_color: tuple[int, int, int]
) -> Image:
    """
    Take a pillow image, square it and add padding with the specified color
    Args:
        image (PIL.Image): Image to process
        background_color (tuple[int, int, int]): color of the padding

    Returns:
        The squared and padded image
    """
    width, height = image.size
    if width == height:
        return image
    elif width > height:
        result = Image.new("RGB", (width, width), background_color)
        result.paste(image, (0, 0))
        return result
    else:
        result = Image.new("RGB", (height, height), background_color)
        result.paste(image, (0, 0))
        return result


class ImageProcessor:
    """
    This class is used to process all the images present
    in the folder passed in the constructor

    Args:
        folder_path (string): The path to the folder that will be processed
    """

    _result_folder_path = "./datasets"

    def __init__(self, folder_path: str):
        self._folderPath = folder_path

    def process_folder(self, img_dimension: int) -> None:
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

        ensure_folder_exists(self._result_folder_path)

        unique_folder_name = datetime.now().strftime("%Y%m%d%H%M%S")
        unique_folder = f"{self._result_folder_path}/{unique_folder_name}/"
        ensure_folder_exists(unique_folder)

        image_sources = os.listdir(self._folderPath)
        for image_source in image_sources:
            processed_image = self._process_image(
                image_source,
                img_dimension,
            )

            processed_image.save(
                f"{unique_folder}/{os.path.basename(image_source)}",
            )

    def _process_image(
        self,
        image_path: str,
        image_dimensions: int,
    ) -> Image:
        """
        Take an image, square it to the wanted dimension
        with padding and return it.

        Args:
            image_path (str): path of the initial image
            image_dimensions (int): size of the wanted to be squared image

        Returns:
            processed image
        """

        image = Image.open(f"{self._folderPath}/{image_path}")
        square_image = _expand_image_to_square(image, (114, 114, 114))
        square_image.resize((image_dimensions, image_dimensions))
        return square_image
