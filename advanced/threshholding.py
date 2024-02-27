import cv2 as cv

# Load the sample image
image = cv.imread('Resources/Photos/cats.jpg')

# Convert the image to grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# simple thresholding
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)

# inverse thresholding
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)

# adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)

# Display the original image and the thresholded images
cv.imshow('Original Image', image)
cv.imshow('Simple Thresholding', thresh)
cv.imshow('Inverse Thresholding', thresh_inv)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)

cv.destroyAllWindows()