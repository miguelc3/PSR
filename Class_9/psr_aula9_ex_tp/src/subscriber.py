#!/usr/bin/env python3

import rospy
from psr_aula9_ex_tp.msg import Dog


def callback(msg):
    rospy.loginfo("Received a dog named " + msg.name + ' which is ' + str(msg.age) +
                  ' years old')


def main():
    # ---------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------

    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber('chatter', Dog, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    main()
