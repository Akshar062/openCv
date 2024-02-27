import cv2 as cv
import numpy as np

image = cv.imread('Resources/Photos/cat.jpg')

cv.imshow('Cat', image)

def translate(image, x, y):
    """
    Function to translate an image by a specified number of pixels in the x and y directions.

    Args:
    image (numpy.ndarray): The image to be translated.
    x (int): The number of pixels to translate the image in the x direction.
    y (int): The number of pixels to translate the image in the y direction.

    -x --> Left.
    -y --> Up.
     x --> Right.
     y --> Down.

    Returns:
    translated (numpy.ndarray): The translated image.
    """
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (image.shape[1], image.shape[0])
    return cv.warpAffine(image, transMat, dimensions)

# rotate the image
def rotate(image, angle, rotation_point=None):
    """
    Function to rotate an image by a specified angle.

    Args:
    image (numpy.ndarray): The image to be rotated.
    angle (float): The angle by which the image is to be rotated.
    rotation_point (tuple): The point about which the image is to be rotated.

    Returns:
    rotated (numpy.ndarray): The rotated image.
    """
    (height, width) = image.shape[:2]
    if rotation_point is None:
        rotation_point = (width // 2, height // 2)
    rotMat = cv.getRotationMatrix2D(rotation_point, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(image, rotMat, dimensions)

# flip the image
flipped = cv.flip(image, 0)
cv.imshow('Flipped', flipped)

translated = translate(image, 100, 100)
cv.imshow('Translated', translated)

rotated = rotate(image, 45)
cv.imshow('Rotated', rotated)

cv.waitKey(0)
cv.destroyAllWindows()
