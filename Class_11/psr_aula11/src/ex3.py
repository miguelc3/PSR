#!/usr/bin/env python3

import math
import rospy
import tf_conversions
import tf2_ros
import geometry_msgs.msg
import turtlesim.msg


def main():
    rospy.init_node('circular_frame')
    br = tf2_ros.TransformBroadcaster()

    t = geometry_msgs.msg.TransformStamped()
    distanceToParent = rospy.get_param('~distanceToParent')
    period = rospy.get_param('~period')

    alpha = 0
    rate = rospy.Rate(100)  # hz
    while not rospy.is_shutdown():
        alpha += (1/period)/100
        if alpha > 2*math.pi:
            alpha = 0

        # Create and populate transformation
        t.header.stamp = rospy.Time.now()
        t.header.frame_id = rospy.remap_name('parent')
        t.child_frame_id = rospy.remap_name('child')
        t.transform.translation.x = distanceToParent * math.cos(alpha)
        t.transform.translation.y = distanceToParent * math.sin(alpha)
        t.transform.translation.z = 0.0
        q = tf_conversions.transformations.quaternion_from_euler(0, 0, 5*alpha)
        t.transform.rotation.x = q[0]
        t.transform.rotation.y = q[1]
        t.transform.rotation.z = q[2]
        t.transform.rotation.w = q[3]

        # Send transformation
        br.sendTransform(t)

        # Sleep
        rate.sleep()

    rospy.spin()


if __name__ == '__main__':
    main()
