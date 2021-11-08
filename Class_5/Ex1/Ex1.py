#!/usr/bin/python3

import cv2

def main():
    image_filename = '../Images/atlas2000_e_atlasmv.png'
    image = cv2.imread(image_filename, cv2.IMREAD_COLOR)  # Load an image

    cv2.imshow('window', image)  # Display the image

    image_bright = image + 20 # Increase brightness
    cv2.imshow('window2', image_bright)

    print(type(image))
    print(image.shape)

    cv2.waitKey(0)  # wait for a key press before proceeding


if __name__ == '__main__':
    main()
