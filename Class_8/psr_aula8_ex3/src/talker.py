#!/usr/bin/python3

# license removed for brevity
import rospy
from std_msgs.msg import String
import argparse


def talker():
    # ===============================
    # Initialization
    # ===============================
    parse = argparse.ArgumentParser(description='PSR argparse example.')
    parse.add_argument('--rate', type=float, help='rate', default=1)
    parse.add_argument('--pub', type=str, help='pub', default='pub1')
    parse.add_argument('--topic', type=str, default='A1')
    parse.add_argument('--message', type=str, default='I don\'t know what to send ')
    args = vars(parse.parse_args())

    print(args)

    pub = rospy.Publisher(args['topic'], String, queue_size=10)
    rospy.init_node(args['pub'], anonymous=True)
    rate = rospy.Rate(args['rate'])  # rate of sending, in hz (times per second)

    # ===============================
    # Execution
    # ===============================
    while not rospy.is_shutdown():
        # build the message to send
        message_to_send = args['message'] + str(rospy.get_time())
        rospy.loginfo(message_to_send)  # print it to the terminal
        pub.publish(message_to_send)  # publish the message
        rate.sleep()  # wait a little bit


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
