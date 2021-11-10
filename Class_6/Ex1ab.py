#!/usr/bin/python3

import cv2 as cv
import argparse


def main():
    parser = argparse.ArgumentParser(description='Part6 Ex1a')
    parser.add_argument('-im', '--image', required=True, type=str, help='Path to the image')
    args = vars(parser.parse_args())

    image = cv.imread(args['image'], cv.IMREAD_COLOR)

    window_name = 'Original'
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
    cv.imshow(window_name, image)

    # Draw a circle
    center_coordinates = (int(image.shape[1]/2), int(image.shape[0]/2))
    print('Center coordinates: ' +  str(center_coordinates))
    radius = 20
    color_cicle = (255, 0, 0)  # Blue in BGR
    thickness = 2

    # Image with circle
    image_modified = cv.circle(image, center_coordinates, radius, color_cicle, thickness)

    # Add text to the image - PSR
    text = 'PSR'
    font = cv.FONT_ITALIC
    coord = (100, 90)
    font_scale = 1
    color_text = (0, 0, 255)  # Red

    # Image wit
    # h text + circle
    image_modified = cv.putText(image_modified, text, coord, font, font_scale, color_text, thickness)

    window_modified = 'Image modified'
    cv.namedWindow(window_modified, cv.WINDOW_AUTOSIZE)
    cv.imshow(window_modified, image_modified)

    cv.waitKey(0)


if __name__ == '__main__':
    main()
