from src.image_processor import ImageProcessor


def main():
    print("Starting program")
    img_processor = ImageProcessor("./input_images")
    img_processor.process_folder(800)
    print("Image processing finished")


if __name__ == "__main__":
    main()
