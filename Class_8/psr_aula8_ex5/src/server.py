#!/usr/bin/env python3

# ======================================
# IMPORT STUFF
# ======================================
from __future__ import print_function
import rospy
from beginner_tutorials.srv import AddTwoInts, AddTwoIntsResponse
import argparse
from psr_aula_ex5.msg import Dog
from psr_aula_ex5.srv import SetDogName, SetDogNameResponse


def change_name(req):
    global dog
    dog.name = req.new_name
    return SetDogNameResponse(True)


def main():

    # ======================================
    # INITIALIZATION
    # ======================================
    parser = argparse.ArgumentParser(description='Client/Server example')
    parser.add_argument('-r', '--rate', type=float, default=1, help='Rate of sending'
                                                                     'messages, in hz')
    args = vars(parser.parse_args())

    global dog
    dog = Dog()
    dog.name = 'Max'
    dog.color = 'Yellow'
    dog.age = 18
    dog.brothers.append('Boby')
    dog.brothers.append('Lily')

    rospy.init_node('talker', anonymous=True)
    pub = rospy.publisher('Chatter', Dog, queue_size=10)
    ser = rospy.Service('name', SetDogName, change_name)

    rate = rospy.Rate(args['rate'])

    # =====================================
    # EXECUTION
    # =====================================
    # Create a dog message to send

    while not rospy.is_shutdown():
        rospy.loginfo(dog)
        pub.publish(dog)

        rate.sleep()


if __name__ == "__main__":
    main()
