import cv2 as cv

class ColorSpaces:
    def __init__(self, image_path):
        self.image = cv.imread(image_path)
        self.gray_image = None
        self.hsv_image = None
        self.lab_image = None
        self.ycrcb_image = None

    def convert_to_gray(self):
        self.gray_image = cv.cvtColor(self.image, cv.COLOR_BGR2GRAY)

    def convert_to_hsv(self):
        self.hsv_image = cv.cvtColor(self.image, cv.COLOR_BGR2HSV)

    def convert_to_lab(self):
        self.lab_image = cv.cvtColor(self.image, cv.COLOR_BGR2LAB)

    def convert_to_ycrcb(self):
        self.ycrcb_image = cv.cvtColor(self.image, cv.COLOR_BGR2YCrCb)

    def convert_hsv_to_bgr(self, hsv_image):
        return cv.cvtColor(hsv_image, cv.COLOR_HSV2BGR)

    def convert_lab_to_bgr(self, lab_image):
        return cv.cvtColor(lab_image, cv.COLOR_LAB2BGR)

    def convert_ycrcb_to_bgr(self, ycrcb_image):
        return cv.cvtColor(ycrcb_image, cv.COLOR_YCrCb2BGR)
    
    def show_images(self):
        cv.imshow('Original Image', self.image)
        cv.imshow('Grayscale Image', self.gray_image)
        cv.imshow('HSV Image', self.hsv_image)
        cv.imshow('L*a*b Image', self.lab_image)
        cv.imshow('YCrCb Image', self.ycrcb_image)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def show_all_combinations(self):
        cv.imshow('Original Image', self.image)
        cv.imshow('Grayscale Image', self.gray_image)
        cv.imshow('HSV Image', self.hsv_image)
        cv.imshow('L*a*b Image', self.lab_image)
        cv.imshow('YCrCb Image', self.ycrcb_image)

        # Convert back to BGR and display
        hsv_to_bgr = self.convert_hsv_to_bgr(self.hsv_image)
        lab_to_bgr = self.convert_lab_to_bgr(self.lab_image)
        ycrcb_to_bgr = self.convert_ycrcb_to_bgr(self.ycrcb_image)

        cv.imshow('HSV to BGR', hsv_to_bgr)
        cv.imshow('L*a*b to BGR', lab_to_bgr)
        cv.imshow('YCrCb to BGR', ycrcb_to_bgr)

        cv.waitKey(0)
        cv.destroyAllWindows()


if __name__ == '__main__':
    image_processor = ColorSpaces('Resources/Photos/cats.jpg')
    image_processor.convert_to_gray()
    image_processor.convert_to_hsv()
    image_processor.convert_to_lab()
    image_processor.convert_to_ycrcb()
    image_processor.show_images()

    # To display all possible combinations
    image_processor.show_all_combinations()
