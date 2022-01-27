#!/usr/bin/env python3

# PSR, Class 10 Ex5
# Miguel Pereira, 88731

import rospy
from std_msgs.msg import String, ColorRGBA, Header
from visualization_msgs.msg import Marker, MarkerArray
from geometry_msgs.msg import Pose, Point, Quaternion, Vector3
import random

back = False

def main():

    # Initialize node
    rospy.init_node('talker', anonymous=True)
    # Create publication
    pub = rospy.Publisher('markers', Marker, queue_size=10)
    rate = rospy.Rate(10)  # 10hz

    global back
    count = 0

    # ============== 2nd marker ===============
    marker2 = Marker()

    # marker2 Header
    marker2.header = Header(stamp=rospy.Time.now(), frame_id='world')

    # marker2 Type
    marker2.type = marker2.SPHERE_LIST

    # marker2 Scale
    marker2.scale = Vector3(x=1, y=1, z=1)

    # marker2 Color
    marker2.color = ColorRGBA(r=1, g=0, b=0, a=0.8)

    # points List
    marker2.points = []
    for i in range(0, 10):
        x = random.randint(-3, 3)
        y = random.randint(-3, 3)
        z = random.randint(-1, 1)
        marker2.points.append(Point(x=x, y=y, z=z))

    # Start publishing
    while not rospy.is_shutdown():

        if not back:
            count += 0.25
        else:
            count -= 0.25

        # ============== 1st marker ===============
        marker = Marker()

        # marker Header
        marker.header = Header(stamp=rospy.Time.now(), frame_id='world')

        # marker Pose
        if count > 3:
            back = True
        elif count < -3:
            back = False

        point = Point(x=count, y=0, z=0)
        quaternion = Quaternion(x=0, y=0, z=0, w=1)
        marker.pose = Pose(position=point, orientation=quaternion)

        # marker Type
        marker.type = Marker.CUBE

        # marker Scale
        marker.scale = Vector3(x=count, y=1, z=1)

        # marker Color
        marker.color = ColorRGBA(r=1, g=0, b=0, a=0.8)

        # marker2 Pose
        point = Point(x=count, y=0, z=0)
        quaternion = Quaternion(x=0, y=0, z=0, w=1)
        marker2.pose = Pose(position=point, orientation=quaternion)

        pub.publish(marker2)
        rospy.loginfo('Publishing marker')

        rate.sleep()


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
