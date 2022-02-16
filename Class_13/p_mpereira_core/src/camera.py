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
        # Set initial variables
        self.bridge = CvBridge()

        # Segment color limits
        self.blue_limits = {'B': {'max': 255, 'min': 100}, 'G': {'max': 50, 'min': 0}, 'R': {'max': 50, 'min': 0}}
        self.red_limits = {'B': {'max': 50, 'min': 0}, 'G': {'max': 50, 'min': 0}, 'R': {'max': 255, 'min': 100}}
        self.green_limits = {'B': {'max': 50, 'min': 0}, 'G': {'max': 255, 'min': 100}, 'R': {'max': 50, 'min': 0}}

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
            self.segmentPlayers(self.cv_image)
        except CvBridgeError as e:
            rospy.logerr("CvBridge Error: {0}".format(e))

        self.show_image(self.cv_image, 'live image')

    def segmentPlayers(self, cv_image):

        # Define maks
        self.blue_mask = cv2.inRange(cv_image,
                                     (self.blue_limits['B']['min'], self.blue_limits['G']['min'],
                                      self.blue_limits['R']['min']),
                                     (self.blue_limits['B']['max'], self.blue_limits['G']['max'],
                                      self.blue_limits['R']['max']))

        self.red_mask = cv2.inRange(cv_image,
                                    (self.red_limits['B']['min'], self.red_limits['G']['min'],
                                     self.red_limits['R']['min']),
                                    (self.red_limits['B']['max'], self.red_limits['G']['max'],
                                     self.red_limits['R']['max']))

        self.green_mask = cv2.inRange(cv_image,
                                      (self.green_limits['B']['min'], self.green_limits['G']['min'],
                                       self.green_limits['R']['min']),
                                      (self.green_limits['B']['max'], self.green_limits['G']['max'],
                                       self.green_limits['R']['max']))

        self.show_image(self.red_mask, 'Red mask')


# =============================
# Main function
# =============================
def main():

    name = rospy.init_node('p_mpereira', anonymous=False)
    camImg = CamImg()
    while not rospy.is_shutdown():
        rospy.spin()


if __name__ == '__main__':
    main()
