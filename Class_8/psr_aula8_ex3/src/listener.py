#!/usr/bin/python3

import rospy
from std_msgs.msg import String
import argparse


def callback(data):
    # This function is called when a message gets to the topic
    rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    # print message in terminal


def listener():
    # ===============================
    # Initialization
    # ===============================
    parse = argparse.ArgumentParser(description='PSR argparse example.')
    parse.add_argument('--sub', type=str, help='sub', default='sub1')
    parse.add_argument('--topic1', type=str, default='A1')
    parse.add_argument('--topic2', type=str)
    args = vars(parse.parse_args())

    print(args)

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.

    # ===============================
    # Initialization
    # ===============================
    rospy.init_node(args['sub'], anonymous=True)  # Initialize node
    rospy.Subscriber(args['topic1'], String, callback)  # Subscribe to topic
    if args['topic2']:
        rospy.Subscriber(args['topic2'], String, callback)
    # Call function callback whenever a message arrives

    # ===============================
    # Execution
    # ===============================
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()
