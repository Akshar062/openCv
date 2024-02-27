import cv2 as cv



# by defult image is read in BGR format

image = cv.imread('Resources/Photos/cat.jpg')

# convert image to grayscale
def convert_to_grayscale(image):
    """
    Function to convert an image to grayscale.

    Args:
    image (numpy.ndarray): The image to be converted.

    Returns:
    gray (numpy.ndarray): The grayscale image.
    """
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    return gray


# blur the image

def blur_image(image, kernel_size):
    """
    Function to blur an image.

    Args:
    image (numpy.ndarray): The image to be blurred.
    kernel_size (tuple): The size of the kernel to be used for blurring.

    Returns:
    blurred (numpy.ndarray): The blurred image.
    """
    blurred = cv.GaussianBlur(image, kernel_size, cv.BORDER_DEFAULT)
    return blurred


# edge cascade
def edge_cascade(image, threshold1, threshold2):
    """
    Function to apply an edge cascade to an image.

    Args:
    image (numpy.ndarray): The image to which the edge cascade is to be applied.
    threshold1 (int): The first threshold for the edge detection algorithm.
    threshold2 (int): The second threshold for the edge detection algorithm.

    Returns:
    edges (numpy.ndarray): The image with the edge cascade applied.
    """
    edges = cv.Canny(image, threshold1, threshold2)
    return edges


# dilate the image
def dilate_image(image, kernel, iterations):
    """
    Function to dilate an image.

    Args:
    image (numpy.ndarray): The image to be dilated.
    kernel (numpy.ndarray): The kernel to be used for dilation.
    iterations (int): The number of iterations for dilation.

    Returns:
    dilated (numpy.ndarray): The dilated image.
    """
    dilated = cv.dilate(image, kernel, iterations=iterations)
    return dilated

# erode the image
def erode_image(image, kernel, iterations):
    """
    Function to erode an image.

    Args:
    image (numpy.ndarray): The image to be eroded.
    kernel (numpy.ndarray): The kernel to be used for erosion.
    iterations (int): The number of iterations for erosion.

    Returns:
    eroded (numpy.ndarray): The eroded image.
    """
    eroded = cv.erode(image, kernel, iterations=iterations)
    return eroded

# resize the image
def resize_image(image, dimensions):
    """
    Function to resize an image.

    Args:
    image (numpy.ndarray): The image to be resized.
    dimensions (tuple): The dimensions to which the image is to be resized.

    Returns:
    resized (numpy.ndarray): The resized image.
    """
    resized = cv.resize(image, dimensions, interpolation=cv.INTER_AREA)
    return resized

# crop the image
def crop_image(image, start_row, end_row, start_col, end_col):
    """
    Function to crop an image.

    Args:
    image (numpy.ndarray): The image to be cropped.
    start_row (int): The starting row index of the region.
    end_row (int): The ending row index of the region.
    start_col (int): The starting column index of the region.
    end_col (int): The ending column index of the region.

    Returns:
    cropped (numpy.ndarray): The cropped image.
    """
    cropped = image[start_row:end_row, start_col:end_col]
    return cropped


# Create a blank image to display all stages
result_image = convert_to_grayscale(image)

# Display each stage in one window
cv.imshow('Original Image', image)
cv.waitKey(0)

# Convert to grayscale
result_image = convert_to_grayscale(image)
cv.imshow('Grayscale Image', result_image)
cv.waitKey(0)

# Blur the image
result_image = blur_image(result_image, (5, 5))
cv.imshow('Blurred Image', result_image)
cv.waitKey(0)

# Apply edge cascade
result_image = edge_cascade(result_image, 50, 150)
cv.imshow('Edge Cascade Image', result_image)
cv.waitKey(0)

# Dilate the image
kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
result_image = dilate_image(result_image, kernel, 1)
cv.imshow('Dilated Image', result_image)
cv.waitKey(0)

# Erode the image
result_image = erode_image(result_image, kernel, 1)
cv.imshow('Eroded Image', result_image)
cv.waitKey(0)

# Resize the image
result_image = resize_image(result_image, (300, 300))
cv.imshow('Resized Image', result_image)
cv.waitKey(0)

# Crop the image
result_image = crop_image(result_image, 50, 250, 50, 250)
cv.imshow('Cropped Image', result_image)
cv.waitKey(0)

# Close all windows
cv.destroyAllWindows()
