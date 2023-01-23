from PIL import Image

def get_pixels(img_path) -> list:
    """
    Return not white pixels from image.
    """
    im = Image.open(img_path)
    image_size_Width, img_size_height = im.size
    pixels = []
    for i in range(1, image_size_Width):
        for j in range(1, img_size_height):
            pixVal = im.getpixel((i, j))
            if pixVal != (255, 255, 255):
                pixels.append([i, j])
    return pixels