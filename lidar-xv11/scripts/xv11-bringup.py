#!/usr/bin/env python
import rospy

# Because of transformations
import tf_conversions
import tf2_ros
import geometry_msgs.msg

import subprocess

subprocess.call(["./motor.sh","on"])

rospy.init_node('tf2_neato_laser_frame_broadcaster')

rospy.loginfo("Motor is started, neato_laser frame is published")

br = tf2_ros.TransformBroadcaster()
t = geometry_msgs.msg.TransformStamped()
t.header.stamp = rospy.Time.now()
t.header.frame_id = "map"
t.child_frame_id = "neato_laser"
t.transform.translation.x = 0
t.transform.translation.y = 0
t.transform.translation.z = 0
t.transform.rotation.x = 0
t.transform.rotation.y = 0
t.transform.rotation.z = 0
t.transform.rotation.w = 1

while not rospy.is_shutdown():
    br.sendTransform(t)
    rospy.sleep(0.1)

subprocess.call(["./motor.sh","off"])

rospy.loginfo('Motor is stopped')
