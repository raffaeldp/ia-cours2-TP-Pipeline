from src.image_processor import ImageProcessor


def main():
    print("coucou")


if __name__ == "__main__":
    main()

    test = ImageProcessor("./input_images")

    test.process_folder(800)
