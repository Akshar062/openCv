import cv2 as cv
import numpy as np

def show_color_channels(image_path):
    # Read the image
    image = cv.imread(image_path)

    # Split the image into BGR channels
    blue_channel, green_channel, red_channel = cv.split(image)

    # Create blank images for each channel
    zeros = np.zeros_like(blue_channel)
    blue_channel_img = cv.merge([blue_channel, zeros, zeros])
    green_channel_img = cv.merge([zeros, green_channel, zeros])
    red_channel_img = cv.merge([zeros, zeros, red_channel])

    # Display the original image and individual color channels
    cv.imshow('Original Image', image)
    cv.imshow('Blue Channel', blue_channel_img)
    cv.imshow('Green Channel', green_channel_img)
    cv.imshow('Red Channel', red_channel_img)

    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    image_path = 'Resources/Photos/cats.jpg'
    show_color_channels(image_path)
