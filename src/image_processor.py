from PIL import Image
import os


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


class ImageProcessor:
    """
    This class is used to process all the images present
    in the folder passed in the constructor

    Args:
        folder_path (string): The path to the folder that will be processed
    """

    _result_folder_path = "./result"

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

        if not os.path.exists(self._result_folder_path):
            os.makedirs(self._result_folder_path)
        else:
            for filename in os.listdir(self._result_folder_path):
                file_path = os.path.join(self._result_folder_path, filename)
                if os.path.isfile(file_path):
                    os.remove(file_path)

        for imageSource in image_sources:
            self._process_image(imageSource, img_dimension)

    def _process_image(self, image_path, image_dimensions):
        image = Image.open(f"{self._folderPath}/{image_path}")
        square_image = _expand2square(image, (114, 114, 114))
        square_image.resize((image_dimensions, image_dimensions))

        savepath = f"{self._result_folder_path}/{os.path.basename(image_path)}"
        square_image.save(savepath)
