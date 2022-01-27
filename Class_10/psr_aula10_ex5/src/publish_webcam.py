#!/usr/bin/env python3

# PSR, Class 10 Ex5
# Miguel Pereira, 88731

# ==================================
# Import libraries
# ==================================
import rospy
import cv2 as cv
from cv_bridge import CvBridge
from sensor_msgs.msg import Image


def main():

    # Initialize the ros node
    rospy.init_node('image_publisher')

    # Setup the point cloud subscriber
    publisher = rospy.Publisher('~image', Image, queue_size=1)

    # Video capture setup
    capture = cv.VideoCapture(0)
    window_name = 'Opencv capture'
    cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)

    # Rate of sending images
    rate = rospy.Rate(15)

    while 1:  # Infinite loop of image acquisition
        _, image = capture.read()  # get image from camera

        cv.imshow(window_name, image)  # display image

        # build message to send
        bridge = CvBridge()
        image_message = bridge.cv2_to_imgmsg(image, encoding='bgr8')
        publisher.publish(image_message)

        key = cv.waitKey(10)
        if key == ord('q'):
            break

        rate.sleep()

    # when everything is done, release the capture
    capture.release()
    cv.destroyAllWindows()

    rospy.spin()


if __name__ == '__main__':
    main()
