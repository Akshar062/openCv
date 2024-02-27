# import libraries
import cv2 as cv
import numpy as np

def draw_blank_image():
    """
    Function to draw a blank image.

    Returns:
    blank (numpy.ndarray): A blank image with dimensions (500, 500, 3).
    """
    blank = np.zeros((500, 500, 3), dtype='uint8')
    return blank

def paint_image(image, coordinates, color):
    """
    Function to paint a single pixel of the image with a specified color.

    Args:
    image (numpy.ndarray): The image to be painted.
    coordinates (tuple): The coordinates of the pixel to be painted.
    color (tuple): The color to be used for painting.

    Returns:
    image (numpy.ndarray): The image with the pixel painted.
    """
    image[coordinates[0], coordinates[1]] = color
    return image

def paint_region(image, start_row, end_row, start_col, end_col, color):
    """
    Function to paint a region of the image with a specified color.

    Args:
    image (numpy.ndarray): The image to be painted.
    start_row (int): The starting row index of the region.
    end_row (int): The ending row index of the region.
    start_col (int): The starting column index of the region.
    end_col (int): The ending column index of the region.
    color (tuple): The color to be used for painting.

    Returns:
    image (numpy.ndarray): The image with the region painted.
    """
    image[start_row:end_row, start_col:end_col] = color
    return image

def draw_rectangle(image, start, end, color, thickness):
    """
    Function to draw a rectangle on the image.

    Args:
    image (numpy.ndarray): The image on which the rectangle is to be drawn.
    start (tuple): The starting coordinates of the rectangle.
    end (tuple): The ending coordinates of the rectangle.
    color (tuple): The color of the rectangle.
    thickness (int): The thickness of the rectangle's edges.

    Returns:
    image (numpy.ndarray): The image with the rectangle drawn.
    """
    cv.rectangle(image, start, end, color, thickness)
    return image

def draw_circle(image, center, radius, color, thickness):
    """
    Function to draw a circle on the image.

    Args:
    image (numpy.ndarray): The image on which the circle is to be drawn.
    center (tuple): The center coordinates of the circle.
    radius (int): The radius of the circle.
    color (tuple): The color of the circle.
    thickness (int): The thickness of the circle's edges.

    Returns:
    image (numpy.ndarray): The image with the circle drawn.
    """
    cv.circle(image, center, radius, color, thickness)
    return image

def draw_line(image, start, end, color, thickness):
    """
    Function to draw a line on the image.

    Args:
    image (numpy.ndarray): The image on which the line is to be drawn.
    start (tuple): The starting coordinates of the line.
    end (tuple): The ending coordinates of the line.
    color (tuple): The color of the line.
    thickness (int): The thickness of the line.

    Returns:
    image (numpy.ndarray): The image with the line drawn.
    """
    cv.line(image, start, end, color, thickness)
    return image

def write_text(image, text, position, font, scale, color, thickness):
    """
    Function to write text on the image.

    Args:
    image (numpy.ndarray): The image on which the text is to be written.
    text (str): The text to be written.
    position (tuple): The position of the text.
    font (int): The font style of the text.
    scale (float): The scale of the text.
    color (tuple): The color of the text.
    thickness (int): The thickness of the text.

    Returns:
    image (numpy.ndarray): The image with the text written.
    """
    cv.putText(image, text, position, font, scale, color, thickness)
    return image

def show_image(title, image):
    """
    Function to display the image.

    Args:
    title (str): The title of the image window.
    image (numpy.ndarray): The image to be displayed.
    """
    cv.imshow(title, image)
    cv.waitKey(0)
    cv.destroyAllWindows()

# Create a blank image
fun_image = draw_blank_image()

# Paint a region with a color
region_color = (0, 255, 0)  # Green
fun_image = paint_region(fun_image, 100, 300, 100, 400, region_color)

# Draw a rectangle
rectangle_start = (50, 50)
rectangle_end = (450, 200)
rectangle_color = (255, 0, 0)  # Blue
fun_image = draw_rectangle(fun_image, rectangle_start, rectangle_end, rectangle_color, thickness=2)

# Draw a circle
circle_center = (250, 350)
circle_radius = 50
circle_color = (0, 0, 255)  # Red
fun_image = draw_circle(fun_image, circle_center, circle_radius, circle_color, thickness=2)

# Draw a line
line_start = (100, 400)
line_end = (400, 400)
line_color = (255, 255, 255)  # White
fun_image = draw_line(fun_image, line_start, line_end, line_color, thickness=3)

# Write text
text_position = (150, 250)
text_color = (255, 255, 255)  # White
font = cv.FONT_HERSHEY_SIMPLEX
fun_image = write_text(fun_image, 'OpenCV Fun', text_position, font, 1, text_color, thickness=2)

# Show the fun image
show_image('Fun Image', fun_image)
