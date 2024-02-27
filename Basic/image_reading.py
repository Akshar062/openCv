# read image

import cv2 as cv
import utils.utils as ut


def read_image(image_path):
    """
    Read an image from the specified path and display it using OpenCV.

    Parameters:
    image_path (str): The path to the image file.

    Returns:
    None
    """
    img = cv.imread(image_path)
    cv.imshow('Image', img)
    cv.imshow('Rescaled Image', ut.rescale_frame(img, 2))
    cv.waitKey(0)
    cv.destroyAllWindows()


# call the function
read_image('Resources/Photos/cat.jpg')
