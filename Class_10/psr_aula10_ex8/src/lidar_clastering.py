#!/usr/bin/env python3

# ==================================
# Import libraries
# ==================================
import rospy
import std_msgs.msg
from sensor_msgs.msg import LaserScan, PointCloud2, PointField
from sensor_msgs import point_cloud2
import math
from visualization_msgs.msg import MarkerArray, Marker
from geometry_msgs.msg import Point
import random

# Create publisher - global variable to use in botch functions
publisher = rospy.Publisher('/markers', MarkerArray, queue_size=1)


def createMarker():
    # Create Marker
    marker = Marker()
    marker.header.frame_id = "left_laser"
    marker.header.stamp = rospy.Time.now()
    marker.ns = "my_namespace"
    marker.id = 0
    marker.type = Marker.SPHERE_LIST
    marker.pose.orientation.w = 1.0  # Otherwise, quaternion is not normalized

    marker.scale.x = 0.2
    marker.scale.y = 0.2
    marker.scale.z = 0.2
    marker.color.a = 0.6
    marker.color.r = random.random()
    marker.color.g = random.random()
    marker.color.b = random.random()

    return marker


def callbackMessageReceived(msg):

    # Received message - notify
    rospy.loginfo('Received laser scan message')

    x_prev, y_prev = 1000, 1000
    dist_thereshold = 0.5

    marker_array = MarkerArray()

    z = 0
    for idx, range in enumerate(msg.ranges):

        if range < 0.1:
            continue

        theta = msg.angle_min + msg.angle_increment * idx
        x = range * math.cos(theta)
        y = range * math.sin(theta)

        # Should I create a new cluster?
        dist = math.sqrt((x_prev-x)**2 + (y_prev-y)**2)
        if dist > dist_thereshold:  # new cluster
            marker = createMarker()
            marker.id = len(marker_array.markers)
            marker.points = []
            marker_array.markers.append(marker)

        last_marker = marker_array.markers[-1]
        last_marker.points.append(Point(x=x, y=y, z=z))

        x_prev = x
        y_prev = y

    # publish message
    publisher.publish(marker_array)

    # Published message - notify
    rospy.loginfo('Published marker array')


def main():

    rospy.init_node('lidar_subscriber', anonymous=False)

    # Create subscriber
    rospy.Subscriber('/left_laser/laserscan', LaserScan, callbackMessageReceived)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    main()
