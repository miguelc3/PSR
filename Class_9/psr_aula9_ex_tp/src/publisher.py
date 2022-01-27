#!/usr/bin/env python3
# source ~/catkin_ws/devel/setup.bash <- para o ros funcionar

import rospy
from std_msgs.msg import String
from psr_aula9_ex_tp.msg import Dog
from colorama import Fore, Style


def main():
    # ---------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------
    rospy.init_node('publisher', anonymous=True)
    pub = rospy.Publisher('chatter', Dog, queue_size=10)

    # read global parameters - "/" behind the name of the parameter
    highlight_text_color = global_name = rospy.get_param('/highlight_text_color')

    # read private parameter - "~" behind the name of the parameter
    frequency = rospy.get_param('~frequency', default=1)
    rate = rospy.Rate(frequency)  # hz

    # ---------------------------------------------------
    # Execution
    # ---------------------------------------------------
    while not rospy.is_shutdown():

        # create a dog message to sent
        dog = Dog()
        dog.name = 'max'
        dog.age = 18
        dog.color = 'black'
        dog.brothers.append('lily')
        dog.brothers.append('boby')

        rospy.loginfo("Publishing dog message with name " +
                      getattr(Fore, highlight_text_color) +
                      dog.name + Style.RESET_ALL)
        pub.publish(dog)
        rate.sleep()

    # ---------------------------------------------------
    # Termination
    # ---------------------------------------------------


if __name__ == '__main__':
    main()
