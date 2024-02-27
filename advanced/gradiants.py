import cv2 as cv
import numpy as np

# Load the sample image
image = cv.imread('Resources/Photos/cats.jpg')

# Convert the image to grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Sobel Gradients
sobel_x = cv.Sobel(gray, cv.CV_64F, 1, 0, ksize=5)

sobel_y = cv.Sobel(gray, cv.CV_64F, 0, 1, ksize=5)

combined_sobel = cv.bitwise_or(sobel_x, sobel_y)

# Laplacian Gradients
laplacian = cv.Laplacian(gray, cv.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))

# Display the original image and the thresholded images
cv.imshow('Original Image', image)
cv.imshow('Sobel X', sobel_x)
cv.imshow('Sobel Y', sobel_y)
cv.imshow('Combined Sobel', combined_sobel)
cv.imshow('Laplacian', laplacian)


cv.waitKey(0)


cv.destroyAllWindows()