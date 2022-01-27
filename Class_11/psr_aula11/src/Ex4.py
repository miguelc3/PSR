#!/usr/bin/env python3

import rospy
import math
import tf2_ros
import geometry_msgs.msg
import turtlesim.srv


def main():
    rospy.init_node('mercury_to_moon')

    tfBuffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(tfBuffer)

    rate = rospy.Rate(1)
    while not rospy.is_shutdown():
        now = rospy.Time.now()
        try:
            # tentar escutar transformação - lookup_transform
            trans = tfBuffer.lookup_transform('Mercury', 'Moon', rospy.Time())
            distance = math.sqrt(trans.transform.translation.x ** 2 +
                                 trans.transform.translation.y ** 2)
            rospy.loginfo('Distance from mercury to moon is ' + str(distance))
            # print(trans.transform.translation)
            # print(trans.transform.rotation)
        except (tf2_ros.LookupException, tf2_ros.ConnectivityException, tf2_ros.ExtrapolationException):
            rospy.logwarn('Could not find transformation')
            rate.sleep()
            continue

        rate.sleep()


if __name__ == '__main__':
    main()
