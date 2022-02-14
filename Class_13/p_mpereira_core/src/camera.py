#!/usr/bin/env python3

# =============================
# Import pkgs
# =============================
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError


class CamImg():

    def __init__(self):
        # =============================
        # Global variables
        # =============================
        self.bridge = CvBridge()

        rospy.init_node('p_mpereira', anonymous=False)
        self.name = rospy.get_name()
        print('My name is ' + self.name)
        self.name = self.name.strip('/')

        self.sub_image = rospy.Subscriber(self.name + "/camera/rgb/image_raw", Image, self.image_callback)

        # self.show_image(self.cv_image, 'live image')

    # =============================
    # Functions
    # =============================
    def show_image(self, img, window_name):
        rospy.loginfo('Going to show image')
        cv2.namedWindow(window_name, 1)
        cv2.imshow(window_name, img)
        cv2.waitKey(3)

    def image_callback(self, img_msg):
        rospy.loginfo('Image Received')

        try:
            self.cv_image = self.bridge.imgmsg_to_cv2(img_msg, "passthrough")
            self.cv_image = cv2.cvtColor(self.cv_image, cv2.COLOR_BGR2RGB)
        except CvBridgeError as e:
            rospy.logerr("CvBridge Error: {0}".format(e))

        self.show_image(self.cv_image, 'live image')


# =============================
# Main function
# =============================
def main():

    camImg = CamImg()
    while not rospy.is_shutdown():
        rospy.spin()


if __name__ == '__main__':
    main()
