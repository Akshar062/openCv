
# function to rescale the frame
import cv2 as cv


# function to rescale the frame 
# works for images, videos and live videos

def rescale_frame(frame, scale=0.75):
    # images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)



