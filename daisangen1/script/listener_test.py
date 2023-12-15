#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64

def area_callback(data):
    rospy.loginfo("Received Area: %f" % data.data)

def cx_callback(data):
    rospy.loginfo("Received CX: %f" % data.data)

def cy_callback(data):
    rospy.loginfo("Received CY: %f" % data.data)

def listener():
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber('/area_topic', Float64, area_callback)
    rospy.Subscriber('/cx_topic', Float64, cx_callback)
    rospy.Subscriber('/cy_topic', Float64, cy_callback)

    rospy.spin()

if __name__ == '__main__':
    listener()
