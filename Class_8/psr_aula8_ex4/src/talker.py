#!/usr/bin/env python3
# source ~/catkin_ws/devel/setup.bash <- para o ros funcionar

import rospy
from psr_aula8_ex4.msg import Dog


def main():
    # ---------------------------------------------------
    # INITIALIZATION
    # ---------------------------------------------------
    rospy.init_node('publisher', anonymous=True)
    pub = rospy.Publisher('politics', Dog, queue_size=10)
    rate = rospy.Rate(1)


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

        rospy.loginfo('Sending dog ...')
        pub.publish(dog)

        rate.sleep()

    # ---------------------------------------------------
    # Termination
    # ---------------------------------------------------


if __name__ == '__main__':
    main()