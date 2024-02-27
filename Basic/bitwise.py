import cv2 as cv
import numpy as np

# Create two images (black and white)
img1 = np.zeros((300, 300), dtype=np.uint8)
img2 = np.zeros((300, 300), dtype=np.uint8)

# Create rectangular regions in the images
cv.rectangle(img1, (50, 50), (250, 250), 255, -1)
cv.circle(img2, (150, 150), 100, 255, -1)

# Bitwise AND
bitwise_and = cv.bitwise_and(img1, img2)

# Bitwise OR
bitwise_or = cv.bitwise_or(img1, img2)

# Bitwise XOR
bitwise_xor = cv.bitwise_xor(img1, img2)

# Bitwise NOT
bitwise_not_img1 = cv.bitwise_not(img1)
bitwise_not_img2 = cv.bitwise_not(img2)

# Display the images and their bitwise operations
cv.imshow('Image 1', img1)
cv.imshow('Image 2', img2)
cv.imshow('Bitwise AND', bitwise_and)
cv.imshow('Bitwise OR', bitwise_or)
cv.imshow('Bitwise XOR', bitwise_xor)
cv.imshow('Bitwise NOT Image 1', bitwise_not_img1)
cv.imshow('Bitwise NOT Image 2', bitwise_not_img2)

cv.waitKey(0)
cv.destroyAllWindows()
