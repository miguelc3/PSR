#!/usr/bin/python3

import cv2 as cv
import argparse

# Global Variables
im_gray = None
window_name = 'Ex3 window'


def on_trackbar(val):
    global im_gray
    _, im_thresholded = cv.threshold(im_gray, val, 255, cv.THRESH_BINARY)
    cv.imshow(window_name, im_thresholded)


def main():

    global im_gray

    # Process arguments
    parser = argparse.ArgumentParser(description='Ex3 opencv')
    parser.add_argument('-im', '--image', type=str, required=True, help='Path to the image')
    args = vars(parser.parse_args())

    # Load image -> RGB
    im = cv.imread(args['image'], cv.IMREAD_COLOR)
    im = cv.cvtColor(im, cv.COLOR_BGR2RGB)
    cv.namedWindow('Original', cv.WINDOW_NORMAL)
    cv.imshow('Original', im)

    # RGB -> Gray
    im_gray = cv.cvtColor(im, cv.COLOR_RGB2GRAY)
    cv.namedWindow('Gray scale', cv.WINDOW_NORMAL)
    cv.imshow('Gray scale', im_gray)

    # Show image with trackbar
    cv.namedWindow(window_name, cv.WINDOW_NORMAL)
    cv.createTrackbar('Threshold', window_name, 0, 255, on_trackbar)

    # Initialize binarized image with threshold o
    on_trackbar()

    cv.waitKey(0)

if __name__ == '__main__':
    main()