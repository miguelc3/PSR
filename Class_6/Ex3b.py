#!/usr/bin/python3

import copy
import numpy as np
import cv2


def main():

    print('Press "q" if you want to exit')

    # Cascade for detecting faces
    face_casc_Path = '/home/miguel/catkin_ws/src/PSR/Class_6/haarcascade_frontalface_default.xml'

    # Create the cascade and initialize it with our face cascade
    face_cascade = cv2.CascadeClassifier(face_casc_Path)

    # Variable to capture video
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame and convert it to gray
        _, frame = video_capture.read()
        frame_gui = copy.deepcopy(frame)

        gray = cv2.cvtColor(frame_gui, cv2.COLOR_BGR2GRAY)
        # Canny to detect adges
        edges = cv2.Canny(gray.copy(), threshold1=50, threshold2=150, apertureSize=3)

        # edges from uint8 to bool
        edges = edges.astype(np.bool)

        # Detect faces in image - this function detects the actual face
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1,
                                              minNeighbors=5, minSize=(30, 30),
                                              flags=cv2.CvFeatureParams_HAAR)

        # faces is a vector of 4 elements - x, y, w and h
        for (x, y, w, h) in faces:
            # Draw blue rectangle around face
            cv2.rectangle(frame_gui, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # Paint edges red
        frame_gui[edges] = (0, 0, 255)

        # Display the resulting frame
        cv2.imshow('Video', frame_gui)

        key = cv2.waitKey(10)
        if key == ord('q'):
            break

    # Release the capture
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
