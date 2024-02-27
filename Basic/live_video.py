# create live preview of the camera

import cv2 as cv

def read_camera():
    """
    Reads the camera feed and displays it in a live preview window.

    Parameters:
    None

    Returns:
    None
    """
    capture = cv.VideoCapture(0) # 0 is the default camera
    while True:
        _, frame = capture.read()
        cv.imshow('Camera', frame)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break

    capture.release()
    cv.destroyAllWindows()

read_camera()
