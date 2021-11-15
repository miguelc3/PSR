#!/usr/bin/python3

import os
import cv2
import copy
import numpy as np


def main():

    print('Press "q" if you want to exit')

    # Cascade for detecting faces
    face_casc_Path = '/home/miguel/catkin_ws/src/PSR/Class_6/haarcascade_frontalface_default.xml'

    # Create the cascade and initialize it with our face cascade
    face_cascade = cv2.CascadeClassifier(face_casc_Path)

    # Cascade for detecting mouth
    mouth_casc_path = '/home/miguel/catkin_ws/src/PSR/Class_6/haarcascade_mcs_mouth.xml'
    mouth_cascade = cv2.CascadeClassifier(mouth_casc_path)

    # Variable to capture video
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame and convert it to gray
        _, frame = video_capture.read()
        frame_gui = copy.deepcopy(frame)

        lines, cols, _ = frame.shape

        gray = cv2.cvtColor(frame_gui, cv2.COLOR_BGR2GRAY)
        # Canny to detect edges
        edges = cv2.Canny(gray.copy(), threshold1=50, threshold2=150, apertureSize=3)

        # edges from uint8 to bool and paint them red
        edges = edges.astype(np.bool)
        # Paint edges red
        frame_gui[edges] = (0, 0, 255)

        # Detect faces in image - this function detects the actual face
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1,
                                              minNeighbors=5, minSize=(30, 30),
                                              flags=cv2.CvFeatureParams_HAAR)

        # faces is a vector of 4 elements - x, y, w and h
        for (x, y, w, h) in faces:
            # Draw blue rectangle around face
            cv2.rectangle(frame_gui, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Create a mask same size as frame all zeros
            mask_face = np.ndarray((lines, cols), dtype=np.uint8)
            mask_face.fill(0)

            # draw a blue rectangle around the face
            mask_face = cv2.rectangle(mask_face, (x, y), (x + w, y + h), 255, -1)

            cv2.add(frame, (-10, 40, -10, 0), dst=frame_gui, mask=mask_face)

        # Detect mouths
        mouth_rects = mouth_cascade.detectMultiScale(gray, 1.7, 11)
        for (x, y, w, h) in mouth_rects:
            y = int(y - 0.15 * h)
            cv2.rectangle(frame_gui, (x, y), (x + w, y + h), (0, 255, 0), 3)

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
