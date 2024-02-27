import cv2 as cv
import numpy as np

class ThresholdedImageProcessor:
    def __init__(self, image_path):
        self.image = cv.imread(image_path)
        self.gray_image = None
        self.thresholded_image = None
        self.contours = None
        self.contours_image = None

    def convert_to_gray(self):
        self.gray_image = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)

    def apply_threshold(self, threshold_value=125):
        _, self.thresholded_image = cv.threshold(self.gray_image, threshold_value, 255, cv.THRESH_BINARY)

    def find_contours(self):
        self.contours, _ = cv.findContours(self.thresholded_image, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    def draw_contours(self, color=(0, 0, 255), thickness=1):
        blank = np.zeros(self.image.shape, dtype='uint8')
        cv.drawContours(blank, self.contours, -1, color, thickness)
        self.contours_image = blank

    def show_images(self):
        cv.imshow('Original Image', self.image)
        cv.imshow('Grayscale Image', self.gray_image)
        cv.imshow('Thresholded Image', self.thresholded_image)
        cv.imshow('Contours Drawn', self.contours_image)
        cv.waitKey(0)
        cv.destroyAllWindows()


class BlurredImageProcessor:
    def __init__(self, image_path):
        self.image = cv.imread(image_path)
        self.blurred_image = None
        self.contours = None
        self.contours_image = None

    def apply_blur(self, kernel_size=(5, 5)):
        self.blurred_image = cv.GaussianBlur(self.image, kernel_size, cv.BORDER_DEFAULT)

    def find_contours(self):
        gray_image = cv.cvtColor(self.blurred_image, cv.COLOR_BGR2GRAY)
        _, thresh = cv.threshold(gray_image, 125, 255, cv.THRESH_BINARY)
        self.contours, _ = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

    def draw_contours(self, color=(0, 0, 255), thickness=1):
        blank = np.zeros(self.image.shape, dtype='uint8')
        cv.drawContours(blank, self.contours, -1, color, thickness)
        self.contours_image = blank

    def show_images(self):
        cv.imshow('Original Image', self.image)
        cv.imshow('Blurred Image', self.blurred_image)
        cv.imshow('Contours Drawn', self.contours_image)
        cv.waitKey(0)
        cv.destroyAllWindows()


def main():
    # Process image using ThresholdedImageProcessor
    thresholded_processor = ThresholdedImageProcessor('Resources/Photos/cats.jpg')
    thresholded_processor.convert_to_gray()
    thresholded_processor.apply_threshold()
    thresholded_processor.find_contours()
    thresholded_processor.draw_contours()
    thresholded_processor.show_images()

    # Process image using BlurredImageProcessor
    blurred_processor = BlurredImageProcessor('Resources/Photos/cats.jpg')
    blurred_processor.apply_blur()
    blurred_processor.find_contours()
    blurred_processor.draw_contours()
    blurred_processor.show_images()


if __name__ == "__main__":
    main()
