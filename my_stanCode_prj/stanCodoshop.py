"""
File: stanCodoshop.py
Name: Joseph_Sung
----------------------------------------------
SC101_Assignment3 Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.
"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns a value that refers to the "color distance" between a pixel and a mean RGB value.

    Input:
        pixel (Pixel): the pixel with RGB values to be compared
        red (int): the average red value of the pixels to be compared
        green (int): the average green value of the pixels to be compared
        blue (int): the average blue value of the pixels to be compared

    Returns:
        dist (float): the "color distance" of a pixel to the average RGB value of the pixels to be compared.
    """

    # Calculate the shortest distance based on coordinates (x,y,z)
    return ((pixel.red-red)**2 + (pixel.green-green)**2 + (pixel.blue-blue)**2)**0.5


def get_average(pixels):
    """
    Given a list of pixels, finds their average red, blue, and green values.

    Input:
        pixels (List[Pixel]): a list of pixels to be averaged

    Returns:
        rgb (List[int]): a list of average red, green, and blue values of the pixels
                        (returns in order: [red, green, blue])
    """

    rgb = [0, 0, 0]
    total = 0

    # Accumulate the RGB values for each pixels
    for pixel in pixels:
        total += 1
        rgb[0] += pixel.red
        rgb[1] += pixel.green
        rgb[2] += pixel.blue

    # Average the total sum
    rgb[0] //= total
    rgb[1] //= total
    rgb[2] //= total

    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest "color distance", which has the closest color to the average.

    Input:
        pixels (List[Pixel]): a list of pixels to be compared
    Returns:
        best (Pixel): the pixel which has the closest color to the average
    """
    # A list containing the three average color values(R/G/B)
    rgb = get_average(pixels)

    # initial value and initial list for getting best pixel
    best_distance = 256
    best_pixel = []

    for pixel in pixels:
        distance = get_pixel_dist(pixel, rgb[0], rgb[1], rgb[2])

        # To obtain the shortest distance and pixel, compare the distance and the best_distance
        if distance < best_distance:
            best_distance = distance
            best_pixel = pixel

    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    
    # ----- YOUR CODE STARTS HERE ----- #

    # each pixels compare their RGB values to get the best value.
    for x in range(width):
        for y in range(height):

            pixel_list = []
            # Extract the values of corresponding pixels(x,y) in each photo and create a pixel_list.
            for i in range(len(images)):
                pixel = images[i].get_pixel(x, y)
                pixel_list.append(pixel)
            # find the best pixel from the list.
            best_pixel = get_best_pixel(pixel_list)

            # put pixels into the blank SampleImage called 'result'.
            blank = result.get_pixel(x, y)
            blank.red = best_pixel.red
            blank.green = best_pixel.green
            blank.blue = best_pixel.blue

    # ----- YOUR CODE ENDS HERE ----- #

    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
