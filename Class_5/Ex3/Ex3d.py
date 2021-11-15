#!/usr/bin/python3

import numpy as np
import cv2 as cv
import argparse
from functools import partial
import json


def trackbar(val, window, image, limits):
    mins = np.array([limits['R']['min'], limits['G']['min'], limits['B']['min']])
    maxs = np.array([limits['R']['max'], limits['G']['max'], limits['B']['max']])

    mins[0] = cv.getTrackbarPos('min R', window)
    maxs[0] = cv.getTrackbarPos('max R', window)
    mins[1] = cv.getTrackbarPos('min G', window)
    maxs[1] = cv.getTrackbarPos('max G', window)
    mins[2] = cv.getTrackbarPos('min B', window)
    maxs[2] = cv.getTrackbarPos('max B', window)

    [limits['R']['min'], limits['G']['min'], limits['B']['min']] = mins
    [limits['R']['max'], limits['G']['max'], limits['B']['max']] = maxs

    print(limits)

    file_name = 'limits.json'
    with open(file_name, 'w') as file_handle:
        print('writing dictionary d to file ' + file_name)
        json.dump(str(limits), file_handle)

    mask = cv.inRange(image, mins, maxs)
    cv.imshow(window, mask)


def main():

    # Inputs for the image
    parser = argparse.ArgumentParser()
    parser.add_argument('-im', '--image', type=str, required=True, help='Full path to image file.')
    args = vars(parser.parse_args())

    # Load image -> change it to rgb
    image_original = cv.imread(args['image'], cv.IMREAD_COLOR)
    image_original = cv.cvtColor(image_original, cv.COLOR_BGR2RGB)
    window_original = 'Original'
    window_segmented = 'Segmented'

    cv.namedWindow(window_original, cv.WINDOW_NORMAL)
    cv.namedWindow(window_segmented, cv.WINDOW_NORMAL)

    cv.imshow(window_original, image_original)

    limits = {'R': {'max': 200, 'min': 100},
              'G': {'max': 200, 'min': 100},
              'B': {'max': 200, 'min': 100}}

    trackbar_partial = partial(trackbar, window=window_segmented, image=image_original, limits=limits)

    cv.createTrackbar('min R', window_segmented, 40, 255, trackbar_partial)
    cv.createTrackbar('max R', window_segmented, 180, 255, trackbar_partial)
    cv.createTrackbar('min G', window_segmented, 40, 255, trackbar_partial)
    cv.createTrackbar('max G', window_segmented, 180, 255, trackbar_partial)
    cv.createTrackbar('min B', window_segmented, 40, 255, trackbar_partial)
    cv.createTrackbar('max B', window_segmented, 180, 255, trackbar_partial)

    # Press any key to close images
    cv.waitKey(0)


if __name__ == '__main__':
    main()
