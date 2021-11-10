#!/usr/bin/python3

# Import stuff
import cv2 as cv


# Main function
def main():

    print('Press "q" if you want to exit')

    # initial setup - define a video capture object
    capture = cv.VideoCapture(0)

    while True:
        # Capture video frame
        _, frame = capture.read()

        # Display frame
        window_name = 'Ex2a'
        cv.imshow(window_name, frame)

        # Press any key to exit
        key = cv.waitKey(10)
        if key == ord('q'):
            print('You typed "q" to exit')
            break

    capture.release()


if __name__ == '__main__':
    main()
