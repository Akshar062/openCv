
# basic example to read video
import cv2 as cv

def read_video(video_path):
    """
    Read and display a video file.

    Parameters:
    video_path (str): The path to the video file.

    Returns:
    None
    """
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

