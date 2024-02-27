
# basic example to read video
import cv2 as cv

# function to read video

def read_video(video_path):
    capture = cv.VideoCapture(video_path)
    while True:
        isTrue, frame = capture.read()
        cv.imshow('Video', frame)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break

    capture.release()
    cv.destroyAllWindows()

# call the function
read_video('Resources/Videos/dog.mp4')