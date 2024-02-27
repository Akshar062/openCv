import cv2 as cv

img = cv.imread('Resources/Photos/group 1.jpg')

cv.imshow('Lady', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Lady', gray)


haar_cascade = cv.CascadeClassifier('advanced\hear_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=5, minNeighbors=1)


print(f'Number of faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('Detected Faces', img)


cv.waitKey(0)

cv.destroyAllWindows()