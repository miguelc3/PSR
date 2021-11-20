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
    parse.add_argument('--topic', type=str, default='A1')
    parse.add_argument('--message', type=str, default='I don\'t know what to send ')
    args = vars(parse.parse_args())

    print(args)

    pub = rospy.Publisher(args['topic'], String, queue_size=10)
    rospy.init_node('Aveiro', anonymous=True)
    rate = rospy.Rate(args['rate'])  # 10hz

    # ===============================
    # Execution
    # ===============================
    while not rospy.is_shutdown():
        hello_str = args['message'] + str(rospy.get_time())
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
