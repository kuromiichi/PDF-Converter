"""Image to PDF Converter

This script accepts a directory containing images as input
and converts all images into a single .pdf file.

Images should be named by a single number (e.g. "1.jpg") and ordered:
"1.jpg" will be the first page, "2.jpg" will be the second and so on.
"""

import os
from PIL import Image


def img_path() -> tuple[str, int]:
    """Get target path

    This function gets the path containing the images that will be converted.
    """
    path = ""
    while not os.path.exists(path):
        path = input("Enter the folder path > ")
    img_num = len(os.listdir(path))
    if img_num == 0:
        print("No images in target directory.")
    return path, img_num


def create_list(path: str, img_num: int) -> tuple:
    """Create list of images

    This function creates a list containing all images but the first one,
    which will be stored separately to call the conversion function.

    It assumes the target directory contains only the images that
    the script will use.

    The function returns both the first image and the list containing
    the rest of images.
    """
    img1 = first_img(path)
    img_list = []
    if img_num > 1:
        for i in range(2, img_num):
            im = Image.open(path + f"/{i}.jpg").convert("RGB")
            img_list.append(im)
    return img1, img_list


def first_img(path: str) -> Image:
    """Create first page

    This function returns a variable that contains the first image and
    will be used to call the conversion function.
    """
    img1 = Image.open(path + "/1.jpg").convert("RGB")
    return img1


def conversion(path: str, img1: Image, img_list: list) -> None:
    """Convert images to PDF

    This function lets the user select a name for the PDF document and calls
    the conversion method.
    """
    name = input("Enter a name for the PDF document > ")
    save_path = f"{path}/{name}.pdf"
    if len(img_list) == 0:
        img1.save(save_path)
    else:
        img1.save(save_path, save_all=True, append_images=img_list)
    print("Document was created successfuly.")


if __name__ == "__main__":
    path, img_num = img_path()
    if img_num > 0:
        img1, img_list = create_list(path, img_num)
        conversion(path, img1, img_list)
