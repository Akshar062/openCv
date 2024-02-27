import cv2 as cv


img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('Park', img)

# avrage
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# Gaussian blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gauss)

# Median blur
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)
cv.destroyAllWindows()
