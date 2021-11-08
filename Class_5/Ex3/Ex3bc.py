#!/usr/bin/python3

import cv2 as cv
import argparse
from functools import partial


def on_trackbar(val, im_gray, window_name):

    _, im_thresholded = cv.threshold(im_gray, val, 255, cv.THRESH_BINARY)
    cv.imshow(window_name, im_thresholded)


def mouse_position(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        print('coords: (x, y) = ' + str(x) + ', ' + str(y))


def main():

    window_name = 'Ex3 window'

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

    # Use partial funcion
    on_trackbar_partial = partial(on_trackbar, im_gray=im_gray, window_name=window_name)

    # Show image with trackbar
    cv.namedWindow(window_name, cv.WINDOW_NORMAL)
    cv.createTrackbar('Threshold', window_name, 0, 255, on_trackbar_partial)

    # Show mouse position
    cv.setMouseCallback(window_name, mouse_position)

    cv.waitKey(0)


if __name__ == '__main__':
    main()
