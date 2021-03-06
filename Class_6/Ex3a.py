#!/usr/bin/python3

import copy
import cv2
import numpy as np


def main():

    # ----------------------------------------------------------
    # INITIALIZATION
    # ----------------------------------------------------------

    print('Press "q" if you want to exit')

    # Cascade for detecting faces
    face_casc_path = '/home/miguel/catkin_ws/src/PSR/Class_6/haarcascade_frontalface_default.xml'

    # Create the cascade and initialize it with our face cascade
    face_cascade = cv2.CascadeClassifier(face_casc_path)

    # Variable to capture video
    video_capture = cv2.VideoCapture(0)  # setup video capture for webcam
    # video_capture = cv2.VideoCapture('test.mp4')  # setup video capture for video file

    # ----------------------------------------------------------
    # EXECUTION
    # ----------------------------------------------------------

    while True:
        # Capture frame-by-frame and convert it to gray
        _, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        lines, cols, _ = frame.shape
        frame_gui = copy.deepcopy(frame)

        # This is just applicable if I use a video capture from video file
        if frame_gui is None:
            print('Video is over, terminating')
            break

        # Detect faces in image - this function detects the actual face
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1,
                                              minNeighbors=5, minSize=(30, 30),
                                              flags=cv2.CvFeatureParams_HAAR)

        mask_face = np.zeros((lines, cols))

        # faces is a vector of 4 elements - x, y, w and h
        for (x, y, w, h) in faces:
            # Draw blue rectangle around face
            cv2.rectangle(frame_gui, (x, y), (x+w, y+h), (255, 0, 0), 2)

            # Create a mask same size as frame all zeros
            mask_face = np.ndarray((lines, cols), dtype=np.uint8)
            mask_face.fill(0)

            # draw a blue rectangle around the face
            mask_face = cv2.rectangle(mask_face, (x, y), (x+w, y+h), 255, -1)

            cv2.add(frame, (-10, 40, -10, 0), dst=frame_gui, mask=mask_face)

        # Display the resulting frame
        cv2.imshow('Video', frame_gui)
        cv2.imshow('Mask face', mask_face)

        key = cv2.waitKey(10)
        if key == ord('q'):
            break

    # ----------------------------------------------------------
    # TERMINATION
    # ----------------------------------------------------------

    # Release the capture
    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
