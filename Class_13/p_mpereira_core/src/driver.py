#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
import tf2_ros
from geometry_msgs.msg import Twist, PoseStamped
import tf2_geometry_msgs
import copy
import math


class Driver():

    def __init__(self):

        self.name = rospy.get_name()
        self.name = self.name.strip('/')

        self.publisher_command = rospy.Publisher('/' + self.name + '/cmd_vel', Twist, queue_size=1)

        self.tf_buffer = tf2_ros.Buffer()
        self.listener = tf2_ros.TransformListener(self.tf_buffer)

        self.goal = PoseStamped()

        self.angle = 0
        self.speed = 0

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

        print('My name is ' + self.name + '. I am team ' + self.my_team + ', I am hunting  ' + str(self.prey_team_players) +
              ' and fleeing from ' + str(self.hunter_team_players))

        exit(0)



def main():

    # =================================
    # INITIALIZATION
    # =================================
    rospy.init_node('p_mpereira', anonymous=False)

    driver = Driver()

    rate = rospy.Rate(10)  # Hz

    rospy.spin()


if __name__ == '__main__':
    main()
