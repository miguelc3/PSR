#!/usr/bin/python3

import cv2 as cv
import argparse
import numpy as np


def mouse_callback(event, x, y, flags, param):

    global image_bgr
    print('Mouse have been moved to coords: (' + str(x) + ', ' + str(y) + ')')
    pix = image_bgr[y, x]
    b = pix[0]
    g = pix[1]
    r = pix[2]
    print('B= ' + str(b) + ',G= ' + str(g) + ',R= ' + str(r))


def main():

    global image_bgr

    # Process arguments
    parser = argparse.ArgumentParser(description='Opencv exercise')
    parser.add_argument('-im', '--image', type=str, required=True, help='Path of the image')
    args = vars(parser.parse_args())

    # Load image
    image_bgr = cv.imread(args['image'], cv.IMREAD_COLOR)

    # Split image on b g r
    image_b, image_g, image_r = cv.split(image_bgr)

    # Values to isolate the green color
    ranges_bgr = {'b': {'min': 0, 'max': 55},
                  'g': {'min': 80, 'max': 256},
                  'r': {'min': 0, 'max': 55}}

    # Processing
    mins_bgr = np.array([ranges_bgr['b']['min'], ranges_bgr['g']['min'], ranges_bgr['r']['min']])
    maxs_bgr = np.array([ranges_bgr['b']['max'], ranges_bgr['g']['max'], ranges_bgr['r']['max']])

    # Apply cv2.inRange
    mask_bgr = cv.inRange(image_bgr, mins_bgr, maxs_bgr)
    # mask to bool
    mask_bgr = mask_bgr.astype(np.bool)

    # Same thing for hsv
    # Convert from bgr to hsv
    image_hsv = cv.cvtColor(image_bgr, cv.COLOR_BGR2HSV)
    image_h, image_s, image_v = cv.split(image_hsv)

    # Values to isolate the hreen box
    ranges_hsv = {'h': {'min': 40, 'max': 180},  # 60 120 180
                  's': {'min': 180, 'max': 255},
                  'v': {'min': 60, 'max': 180}}

    mins_hsv = np.array([ranges_hsv['h']['min'], ranges_hsv['s']['min'], ranges_hsv['v']['min']])
    maxs_hsv = np.array([ranges_hsv['h']['max'], ranges_hsv['s']['max'], ranges_hsv['v']['max']])
    image_processed_hsv = cv.inRange(image_hsv, mins_hsv, maxs_hsv)

    # New image which will contain only the copy of the masked pixels
    print(image_bgr.dtype)
    print(mask_bgr.dtype)
    # Replace green box for red
    image_red = cv.imread(args['image'], cv.IMREAD_COLOR)
    # Put green box brighter
    # image_red[mask_bgr] = image_red[mask_bgr]*1.5
    image_red[mask_bgr] = (0, 0, 255)
    # All black except green box
    image_black = cv.imread(args['image'], cv.IMREAD_COLOR)
    # Put everything but the box darker
    # image_black[np.logical_not(mask_bgr)] = image_black[np.logical_not(mask_bgr)]*0.5
    image_black[np.logical_not(mask_bgr)] = (0, 0, 0)

    # Show images
    # Original
    cv.namedWindow('Original', cv.WINDOW_GUI_EXPANDED)
    cv.setMouseCallback('Original', mouse_callback)  # to show b g and r values
    cv.imshow('Original', image_bgr)
    # RGB processed - just the green box
    cv.namedWindow('Image processed RGB', cv.WINDOW_AUTOSIZE)
    cv.imshow('Image processed RGB', mask_bgr.astype(np.uint8)*255)
    # HSV processed - just the green box
    cv.imshow('Processed image hsv', image_processed_hsv)
    # Replace green for red
    cv.imshow('Green box - red', image_red)
    # All black except green box
    cv.imshow('Black', image_black)

    cv.waitKey(0)


if __name__ == '__main__':
    main()
