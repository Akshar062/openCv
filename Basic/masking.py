import cv2 as cv
import numpy as np

# Create a sample image
image = cv.imread('Resources/Photos/cats.jpg')

# Create a mask with a circular region
mask = np.zeros_like(image, dtype=np.uint8)
cv.circle(mask, (300, 200), 100, (255, 255, 255), thickness=-1)

# Apply the mask using bitwise AND
masked_image = cv.bitwise_and(image, mask)

# Display the original image, mask, and the masked image
cv.imshow('Original Image', image)
cv.imshow('Mask', mask)
cv.imshow('Masked Image', masked_image)

cv.waitKey(0)
cv.destroyAllWindows()
