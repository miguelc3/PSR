#!/usr/bin/python3
import cv2
import cv2 as cv
import numpy as np
from functools import partial

# Global variable
drawing = False


def draw(event, x, y, flags, param, color):

    #drawing = False
    global drawing

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        print('Started painting at: (x, y) = ' + str(x) + ', ' + str(y))
        param[y, x] = color

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing:
            param[y, x] = color

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        print('Ended painting at: (x, y) = ' + str(x) + ', ' + str(y))


def main():
    print('Click to paint a pixel, press continually to draw lines \n'
          'Press "r" to paint red \n'
          'Press "g" to paint green \n'
          'Press "g" to paint blue \n'
          'Press "q" to quit \n'
          'Starting to paint black \n')

    # Create a white image
    image_white = np.zeros([400, 600, 3], dtype=np.uint8)
    image_white.fill(255)

    window_name = 'White sheet'
    cv.namedWindow(window_name, cv.WINDOW_NORMAL)
    cv.imshow(window_name, image_white)

    color = (0, 0, 0)
    while True:

        key = cv2.waitKey(10)

        if key == ord('q'):
            print('You quited')
            break
        elif key == ord('r'):
            color = (0, 0, 255)
            print('You switched color to red')
        elif key == ord('g'):
            color = (0, 255, 0)
            print('You switched color to green')
        elif key == ord('b'):
            color = (255, 0, 0)
            print('You switched color to blue')

        draw_partial = partial(draw, color=color)
        cv.setMouseCallback(window_name, draw_partial, param=image_white)

        cv.imshow(window_name, image_white)


if __name__ == '__main__':
    main()
