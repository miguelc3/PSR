#!/usr/bin/env python3

import argparse
import rospy
from std_msgs.msg import String
from psr_aula8_ex5.msg import Dog
from psr_aula8_ex5.srv import *
import sys


def callbackMsgReceived(msg):
    rospy.loginfo("Received a dog named " + msg.name + ' which is ' + str(msg.age) +
                  ' years old')


def main():
    # ---------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------
    parser = argparse.ArgumentParser(description='PSR argparse example.')
    parser.add_argument('--topic', type=str, default='chatter')
    parser.add_argument('--name', type=str, default="Sr. Pintarolas")
    args = vars(parser.parse_args())

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber(args['topic'], Dog, callbackMsgReceived)

    rospy.wait_for_service('name')
    name = rospy.ServiceProxy('name', SetDogName)

    resp1 = name(args["name"])


if __name__ == '__main__':
    main()