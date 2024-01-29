# Script to load an image, and then converts it into a vector
# The image size must be 28x28 pixels, and the output vector will be 784 elements long

from PIL import Image


def img_to_vector(img_path: str) -> list:
    img = Image.open(img_path)
    img = img.resize((28, 28))
    img = img.convert('L')

    pixels = list(img.getdata())
    pixel_sum = sum(pixels)
    pixels = [float(x) / pixel_sum for x in pixels]
    return pixels


if __name__ == '__main__':
    print(img_to_vector('./input.png'))
