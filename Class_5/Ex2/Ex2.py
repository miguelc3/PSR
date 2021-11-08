#!/usr/bin/python3

import cv2
import argparse


def main():

    # Process arguments
    parser = argparse.ArgumentParser(description='Opencv example')
    parser.add_argument('-im', '--image', type=str, help='Path to the image')
    args = vars(parser.parse_args())

    # Load Image
    image_rgb = cv2.imread(args['image'], cv2.IMREAD_COLOR)  # Load an image
    image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_BGR2GRAY)  # Original image to gray

    # 2c) - split the image in the 3 channels
    image_b, image_g, image_r = cv2.split(image_rgb)

    # 2b)
    print('Image rbg shape: ' + str(image_rgb.shape))
    print('Image rbg type: ' + str(type(image_rgb)))
    print('Image rbg dtype: ' + str(image_rgb.dtype))  # data type: numpy.ndarray
    print('Image r shape: ' + str(image_r.shape))

    # Process image - 2a)
    _, image_b_processed = cv2.threshold(image_b, 50, 255, cv2.THRESH_BINARY)
    _, image_g_processed = cv2.threshold(image_g, 100, 255, cv2.THRESH_BINARY)
    _, image_r_processed = cv2.threshold(image_r, 150, 255, cv2.THRESH_BINARY)

    new_image_rbg = cv2.merge((image_b_processed, image_g_processed, image_r_processed))

    # Visualization
    cv2.imshow('Original', image_rgb)  # Original image
    cv2.imshow('Gray original image', image_gray)  # Original image to gray
    cv2.imshow('Processed b', image_b_processed)  # Blue channel
    cv2.imshow('Processed g', image_g_processed)  # Green channel
    cv2.imshow('Processed r', image_r_processed)  # Red channel
    cv2.imshow('New image rgb', new_image_rbg)  # Image after being processed

    cv2.waitKey(0)


if __name__ == '__main__':
    main()
