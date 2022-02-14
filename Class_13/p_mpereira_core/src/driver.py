#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import tf2_ros
from geometry_msgs.msg import Twist, PoseStamped
from sensor_msgs.msg import Image
from sensor_msgs.msg import LaserScan
from cv_bridge import CvBridge
import cv2
import numpy as np
import tf2_geometry_msgs
import copy
import math


class Driver():

    def __init__(self):

        self.name = rospy.get_name()
        self.name = self.name.strip('/')
        rospy.sleep(0.2)

        self.publisher_command = rospy.Publisher('/' + self.name + '/cmd_vel', Twist, queue_size=1)
        rospy.Subscriber(self.name + "/camera/rgb/image_raw", Image, self.ImageCallback)
        rospy.Subscriber(self.name + "/scan", LaserScan, self.lidarCallback)

        # Initializa variables
        self.existImage = False

        # Segment color limits
        self.blue_limits = {'B': {'max': 255, 'min': 100}, 'G': {'max': 50, 'min': 0}, 'R': {'max': 50, 'min': 0}}
        self.red_limits = {'B': {'max': 50, 'min': 0}, 'G': {'max': 50, 'min': 0}, 'R': {'max': 255, 'min': 100}}
        self.green_limits = {'B': {'max': 50, 'min': 0}, 'G': {'max': 255, 'min': 100}, 'R': {'max': 50, 'min': 0}}

        self.subState = None

        # =============================
        # Decide team
        # =============================
        red_team = rospy.get_param('/red_players')
        green_team = rospy.get_param('/green_players')
        blue_team = rospy.get_param('/blue_players')
        self.my_team = None  # Just to initialize the variable

        if self.name in red_team:
            self.my_team = 'red'
            self.my_teams_player = red_team
            self.prey_team_players = green_team
            self.hunter_team_players = blue_team
        elif self.name in green_team:
            self.my_team = 'green'
            self.my_teams_player = green_team
            self.prey_team_players = blue_team
            self.hunter_team_players = red_team
        elif self.name in blue_team:
            self.my_team = 'blue'
            self.my_teams_player = blue_team
            self.prey_team_players = red_team
            self.hunter_team_players = green_team
        else:
            rospy.logerr('Something is wrong, I\'m not on the player\'s list')
            exit(0)

        print('My name is ' + self.name + '. I am team ' + self.my_team + ', I am hunting  ' +
              str(self.prey_team_players) + ' and fleeing from ' + str(self.hunter_team_players))

        rospy.Timer(rospy.Duration(0.1), self.print_state, oneshot=False)

    # ===============================
    # CALLBACK FUNCTIONS
    # ===============================

    def imageCallback(self, msg):

        bridge = CvBridge()
        self.cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')

        # Define maks
        self.blue_mask = cv2.inRange(self.cv_image,
                            (self.blue_limits['B']['min'], self.blue_limits['G']['min'], self.blue_limits['R']['min']),
                            (self.blue_limits['B']['max'], self.blue_limits['G']['max'], self.blue_limits['R']['max']))

        self.red_mask = cv2.inRange(self.cv_image,
                            (self.red_limits['B']['min'], self.red_limits['G']['min'], self.red_limits['R']['min']),
                            (self.red_limits['B']['max'], self.red_limits['G']['max'], self.red_limits['R']['max']))

        self.green_mask = cv2.inRange(self.cv_image,
                            (self.green_limits['B']['min'], self.green_limits['G']['min'], self.green_limits['R']['min']),
                            (self.green_limits['B']['max'], self.green_limits['G']['max'], self.green_limits['R']['max']))

        self.existImage = True

    def lidarCallback(self, msg):

        angle = msg.angle_min

        if msg.ranges[0] < 1.3:
            self.subState = "escape_wall"
        else:
            self.subState = None

    def getCentroif(self):
        pass
        # Just run the code if there is an image
        # if self.existImage:



def main():

    # =================================
    # INITIALIZATION
    # =================================
    rospy.init_node('p_mpereira', anonymous=False)
    driver = Driver()

    rospy.spin()


if __name__ == '__main__':
    main()
