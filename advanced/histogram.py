import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def create_circular_mask(image_shape, center, radius):
    mask = np.zeros(image_shape, dtype=np.uint8)
    cv.circle(mask, center, radius, 255, thickness=-1)
    return mask

def plot_histogram(title, xlabel, ylabel, hist, color='b'):
    plt.figure()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.plot(hist, color=color)
    plt.xlim([0, 256])
    plt.show()

def calculate_and_plot_grayscale_histogram(image, mask):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    hist = cv.calcHist([gray], [0], mask, [256], [0, 256])
    plot_histogram('Grayscale Histogram', 'Bins', '# of Pixels', hist)

def calculate_and_plot_color_histogram(image, mask):
    B, G, R = cv.split(image)
    hist_B = cv.calcHist([B], [0], mask, [256], [0, 256])
    hist_G = cv.calcHist([G], [0], mask, [256], [0, 256])
    hist_R = cv.calcHist([R], [0], mask, [256], [0, 256])
    
    plot_histogram('Color Histogram', 'Bins', '# of Pixels', hist_B, 'b')
    plot_histogram('Color Histogram', 'Bins', '# of Pixels', hist_G, 'g')
    plot_histogram('Color Histogram', 'Bins', '# of Pixels', hist_R, 'r')

def main():
    # Load the sample image
    image = cv.imread('Resources/Photos/cats.jpg')

    # Create a circular mask
    mask_center = (300, 200)
    mask_radius = 100
    circular_mask = create_circular_mask(image.shape[:2], mask_center, mask_radius)

    # Calculate and plot the grayscale histogram
    calculate_and_plot_grayscale_histogram(image, circular_mask)

    # Calculate and plot the color histogram
    calculate_and_plot_color_histogram(image, circular_mask)

if __name__ == "__main__":
    main()
