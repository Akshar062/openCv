# read image

import cv2 as cv


# function to read image
def read_image(image_path):
    img = cv.imread(image_path)
    cv.imshow('Image', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


# call the function
read_image('Resources/Photos/cat.jpg')

