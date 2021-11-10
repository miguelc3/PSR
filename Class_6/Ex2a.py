#!/usr/bin/python3

# Import stuff
import cv2 as cv


# Main function
def main():

    # initial setup - define a video capture object
    capture = cv.VideoCapture(0)
    # Capture image
    _, image = capture.read()

    # Show image
    window_name = 'Ex2a'
    cv.imshow(window_name, image)

    # Press any key to exit
    cv.waitKey(0)
    capture.release()


if __name__ == '__main__':
    main()
